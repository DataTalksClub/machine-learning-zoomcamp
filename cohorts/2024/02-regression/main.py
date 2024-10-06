from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import polars as pl
import numpy as np
import os


_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class DataPreparer:
    """
    Prepares a dataset for machine learning, including shuffling, imputing null values,
    scaling features, and splitting the data into training, validation, and test sets.

    Parameters
    ----------
    df : pl.DataFrame
        Polars DataFrame with the data.
    target_column : str
        Name of the target column.

    Methods
    -------
    shuffle(seed: int = 42) -> DataPreparer:
        Shuffles the DataFrame.

    impute_nulls(method: str = 'mean', columns: list = None) -> DataPreparer:
        Imputes null values in specified columns.

    scale_features(columns: list = None) -> DataPreparer:
        Scales numeric features using StandardScaler.

    split_data(train_frac: float = 0.6, val_frac: float = 0.2) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        Splits the dataset into training, validation, and test sets.

    prepare_X_y(df: pl.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        Separates the features (X) and the target (y).
    """

    def __init__(self, df: pl.DataFrame, target_column: str) -> None:
        self.df = df
        self.target_column = target_column

    def shuffle(self, seed: int = 42) -> 'DataPreparer':
        print(f"Shuffling with seed {seed}")
        self.df = self.df.sample(fraction=1, seed=seed, shuffle=True)
        return self

    def impute_nulls(self, method: str = 'mean', columns: list = None) -> 'DataPreparer':
        if columns is None:
            columns = self.df.columns
        for column in columns:
            if method == 'mean':
                imputer = SimpleImputer(strategy='mean')
            elif method == 'zeros':
                imputer = SimpleImputer(strategy='constant', fill_value=0)
            else:
                raise ValueError("Method must be 'mean' or 'zeros'.")
            imputed_data = imputer.fit_transform(
                self.df[column].to_numpy().reshape(-1, 1))
            self.df = self.df.with_columns(
                pl.Series(column, imputed_data.flatten()))
        return self

    def scale_features(self, columns: list = None) -> 'DataPreparer':
        if columns is None:
            columns = [col for col in self.df.columns if col !=
                       self.target_column]
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.df.select(columns).to_numpy())
        self.df = self.df.with_columns(
            [pl.Series(col, scaled_data[:, idx]) for idx, col in enumerate(columns)])
        return self

    def split_data(self, train_frac: float = 0.6, val_frac: float = 0.2) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        n = len(self.df)
        n_train = int(train_frac * n)
        n_val = int(val_frac * n)
        n_test = n - n_train - n_val
        df_train = self.df[:n_train].clone()
        df_val = self.df[n_train:n_train + n_val].clone()
        df_test = self.df[n_train + n_val:].clone()
        return df_train, df_val, df_test

    def prepare_X_y(self, df: pl.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        X = df.select([col for col in df.columns if col !=
                      self.target_column]).to_numpy()
        y = df.select(self.target_column).to_numpy().flatten()
        return X, y


class LinearRegressionModel:
    """
    Implements Linear Regression with optional L2 (Ridge) or L1 (Lasso) regularization.

    Parameters
    ----------
    regularization_type : str, optional
        Type of regularization ('ridge' for L2 or 'lasso' for L1), by default None (no regularization).
    r : float, optional
        Regularization parameter, by default 0 (no regularization).

    Methods
    -------
    train(X: np.ndarray, y: np.ndarray) -> None:
        Trains the linear regression model.
    predict(X: np.ndarray) -> np.ndarray:
        Makes predictions based on the trained model.
    rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        Calculates the Root Mean Squared Error (RMSE).
    """

    def __init__(self, regularization_type: str = None, r: float = 0.0) -> None:
        self.w_0 = None
        self.w = None
        self.regularization_type = regularization_type  # 'ridge' or 'lasso'
        self.r = r  # Regularization strength

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Trains linear regression with optional L2 (Ridge) or L1 (Lasso) regularization.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix (with shape [n_samples, n_features]).
        y : np.ndarray
            Target vector (with shape [n_samples]).
        """
        ones = np.ones(X.shape[0])
        X = np.column_stack([ones, X])

        if self.regularization_type == 'ridge':
            # Ridge (L2): (X.T X + r * I)^{-1} X.T y
            XTX = X.T.dot(X) + self.r * np.eye(X.shape[1])
            XTX_inv = np.linalg.inv(XTX)
            self.w = XTX_inv.dot(X.T).dot(y)
        elif self.regularization_type == 'lasso':
            # Lasso (L1): Requires iterative optimization (simplified using coordinate descent)
            from sklearn.linear_model import Lasso
            model = Lasso(alpha=self.r)
            model.fit(X, y)
            self.w = np.concatenate(([model.intercept_], model.coef_[1:]))
        else:
            # No regularization: (X.T X)^{-1} X.T y
            XTX = X.T.dot(X)
            XTX_inv = np.linalg.inv(XTX)
            self.w = XTX_inv.dot(X.T).dot(y)

        self.w_0, self.w = self.w[0], self.w[1:]

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Makes predictions using the trained model.

        Parameters
        ----------
        X : np.ndarray
            Feature matrix (with shape [n_samples, n_features]).

        Returns
        -------
        np.ndarray
            Predictions (with shape [n_samples]).
        """
        return self.w_0 + X.dot(self.w)

    def rmse(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Calculates the Root Mean Squared Error (RMSE).

        Parameters
        ----------
        y_true : np.ndarray
            Ground truth target values (with shape [n_samples]).
        y_pred : np.ndarray
            Predicted target values (with shape [n_samples]).

        Returns
        -------
        float
            The RMSE value.
        """
        error = y_pred - y_true
        mse = (error ** 2).mean()
        return np.sqrt(mse)


class MLPipeline:
    """
    A pipeline to orchestrate the data preparation and model training workflow, supporting multiple models.

    Methods
    -------
    run_pipeline(train_frac: float = 0.6, val_frac: float = 0.2, impute_method: str = 'mean', scale: bool = False, model_type: str = 'linear_regression', regularization_type: str = None, r: float = 0.0, use_validation_set_for_training: bool = False):
        Runs the full pipeline, including data preparation, model training, and evaluation.
    """

    def __init__(self, df: pl.DataFrame, target_column: str) -> None:
        """
        Initialize the pipeline with a dataset and the target column.

        Parameters
        ----------
        df : pl.DataFrame
            Polars DataFrame with the dataset.
        target_column : str
            Name of the target column (dependent variable).
        """
        self.df = df
        self.target_column = target_column

    def run_pipeline(self,
                     shuffle_seed: int = 42,
                     train_frac: float = 0.6,
                     val_frac: float = 0.2,
                     impute_method: str = 'mean',
                     scale: bool = False,
                     model_type: str = 'linear_regression',
                     regularization_type: str = None,
                     r: float = 0.0,
                     use_validation_set_for_training: bool = False) -> None:
        """
        Runs the full pipeline, including data preparation, model training, and evaluation.

        Parameters
        ----------
        train_frac : float, optional
            Fraction of the data to use for training, by default 0.6.
        val_frac : float, optional
            Fraction of the data to use for validation, by default 0.2.
        impute_method : str, optional
            Method to impute null values ('mean' or 'zeros'), by default 'mean'.
        scale : bool, optional
            Whether to scale the features, by default False.
        model_type : str, optional
            Type of model to use for training ('linear_regression', 'logistic_regression'), by default 'linear_regression'.
        regularization_type : str, optional
            Type of regularization ('ridge' for L2 or 'lasso' for L1), by default None (no regularization).
        r : float, optional
            Regularization parameter, by default 0 (no regularization).
        use_validation_set_for_training : bool, optional
            If True, combine the training and validation sets to use them both for training, by default False.

        Example
        -------
        >>> pipeline = MLPipeline(df, target_column='median_house_value')
        >>> pipeline.run_pipeline(train_frac=0.6, val_frac=0.2, impute_method='mean', scale=True, model_type='linear_regression', regularization_type='ridge', r=0.1, use_validation_set_for_training=True)
        """
        # Step 1: Data Preparation
        preparer = DataPreparer(self.df, self.target_column)
        preparer.shuffle(seed=shuffle_seed).impute_nulls(method=impute_method)

        if scale:
            preparer.scale_features()

        df_train, df_val, df_test = preparer.split_data(train_frac=train_frac, val_frac=val_frac)

        # Step 2: Combine training and validation sets if use_validation_set_for_training is True
        if use_validation_set_for_training:
            df_train = pl.concat([df_train, df_val])  # Combine training and validation sets
            print("Using both training and validation sets for training.")

        # Step 3: Prepare X and y
        X_train, y_train = preparer.prepare_X_y(df_train)
        X_val, y_val = preparer.prepare_X_y(df_val)

        # Step 4: Choose the model based on model_type and regularization
        model = self._select_model(model_type, regularization_type, r)

        # Step 5: Train the model
        model.train(X_train, y_train)

        # Step 6: Make Predictions on Validation Set
        y_pred_val = model.predict(X_val)

        # Step 7: Evaluate Model
        rmse_val = model.rmse(y_val, y_pred_val)
        print(f"RMSE on Validation Set: {rmse_val:.4f}")

        return rmse_val
        

    def _select_model(self, model_type: str, regularization_type: str = None, r: float = 0.0):
        """
        Selects the appropriate model based on the model_type and regularization parameters.

        Parameters
        ----------
        model_type : str
            Type of model ('linear_regression', 'logistic_regression', etc.).
        regularization_type : str, optional
            Type of regularization ('ridge' for L2 or 'lasso' for L1), by default None (no regularization).
        r : float, optional
            Regularization parameter, by default 0 (no regularization).

        Returns
        -------
        model : object
            An instance of the selected model.

        Raises
        ------
        ValueError
            If the provided model_type is not supported.
        """
        # Dictionary of supported models
        model_dict = {
            'linear_regression': LinearRegressionModel(regularization_type=regularization_type, r=r),
            # 'logistic_regression': LogisticRegressionModel(),  # Extendable to other models
            # Add other models here as needed
        }

        if model_type not in model_dict:
            raise ValueError(f"Model type '{model_type}' is not supported.")

        return model_dict[model_type]



if __name__ == '__main__':
    cols = ['ram', 'storage', 'screen', 'final_price']
    df = pl.read_csv(_CURRENT_DIR + '/laptops.csv')
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    pipeline = MLPipeline(df=df[cols],
                          target_column='final_price')

    res = pipeline.run_pipeline(
        shuffle_seed=9,
        train_frac=0.6,
        val_frac=0.2,
        impute_method='zeros',
        scale=True,
        model_type='linear_regression',
        regularization_type='ridge',
        r=0.001,
        use_validation_set_for_training=True
    )
    
    print(res)
