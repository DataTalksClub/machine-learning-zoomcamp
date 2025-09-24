# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Set matplotlib style for better visualizations
plt.style.use('seaborn-v0_8')

# Load the car data from CSV file
print("Loading car data...")
df = pd.read_csv('car_data.csv')
print(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")

# Display the first few rows to understand the data structure
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Get basic information about the dataset
print("\nDataset info:")
print(df.info())

# Get descriptive statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Check for missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())

# Display columns with missing values (only those that have missing values)
missing_cols = df.isnull().sum()[df.isnull().sum() > 0]
print("\nColumns with missing values:")
print(missing_cols)

# Visualize missing values using missingno library (if available)
try:
    import missingno as msno
    print("\nVisualizing missing values...")
    msno.matrix(df)
    plt.title("Missing Values Matrix")
    plt.show()
    
    msno.bar(df)
    plt.title("Missing Values Bar Chart")
    plt.show()
    
    msno.heatmap(df)
    plt.title("Missingness Correlation Heatmap")
    plt.show()
    
    msno.dendrogram(df)
    plt.title("Missingness Dendrogram")
    plt.show()
except ImportError:
    print("Missingno library not available. Skipping missing value visualizations.")

# Set up validation framework
# Split data into train (60%), validation (20%), and test (20%) sets
print("\nSetting up validation framework...")
n = len(df)  # Total number of samples
n_val = int(0.2 * n)  # 20% for validation
n_test = int(0.2 * n)  # 20% for test
n_train = n - n_val - n_test  # 60% for training

print(f"Training set size: {n_train}")
print(f"Validation set size: {n_val}")
print(f"Test set size: {n_test}")

# Shuffle the data to ensure random distribution
print("\nShuffling data...")
np.random.seed(2)  # Set seed for reproducibility
idx = np.arange(n)  # Create array of indices
np.random.shuffle(idx)  # Shuffle the indices

# Split the shuffled data into train, validation, and test sets
df_shuffled = df.iloc[idx]  # Reorder dataframe using shuffled indices
df_val = df_shuffled.iloc[:n_val]  # First 20% for validation
df_test = df_shuffled.iloc[n_val:n_val+n_test]  # Next 20% for test
df_train = df_shuffled.iloc[n_val+n_test:]  # Remaining 60% for training

# Reset index for all dataframes to avoid issues later
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

print("Data split completed.")

# Exploratory Data Analysis (EDA)
print("\nPerforming Exploratory Data Analysis...")

# Clean string columns by converting to lowercase and replacing spaces with underscores
print("Cleaning string columns...")
string_columns = df.select_dtypes(include=['object']).columns
for col in string_columns:
    df[col] = df[col].str.lower().str.replace(" ", "_")
    df_train[col] = df_train[col].str.lower().str.replace(" ", "_")
    df_val[col] = df_val[col].str.lower().str.replace(" ", "_")
    df_test[col] = df_test[col].str.lower().str.replace(" ", "_")

print("String columns cleaned.")

# Visualize the distribution of car prices (MSRP)
print("\nVisualizing price distribution...")
plt.figure(figsize=(10, 6))
sns.histplot(df.msrp[df.msrp < 100000], bins=50)  # Filter out extremely high prices for better visualization
plt.title('Distribution of Car Prices (MSRP)')
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.show()

# Apply log transformation to price to reduce skewness and stabilize variance
print("\nApplying log1p transformation to price...")
# np.log1p is log(1 + x), which handles zero values better than log(x)
price_log = np.log1p(df.msrp)
print("First 5 log-transformed prices:")
print(price_log.head())

# Visualize the log-transformed price distribution
plt.figure(figsize=(10, 6))
sns.histplot(price_log, bins=50)
plt.title('Distribution of Log-Transformed Car Prices')
plt.xlabel('Log(1 + Price)')
plt.ylabel('Count')
plt.show()

# Prepare target variables (log-transformed prices) for train, validation, and test sets
print("\nPreparing target variables...")
y_train = np.log1p(df_train.msrp.values)  # Log-transform training prices
y_val = np.log1p(df_val.msrp.values)      # Log-transform validation prices
y_test = np.log1p(df_test.msrp.values)    # Log-transform test prices

# Remove the target variable (msrp) from feature sets
# This is important to prevent data leakage in supervised learning
del df_train['msrp']
del df_val['msrp']
del df_test['msrp']

print("Target variables prepared.")

# Define base features for the model
base_features = ['engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
print(f"\nBase features: {base_features}")

# Define categorical variables for one-hot encoding
categorical_vars = ['make', 'engine_fuel_type', 'transmission_type', 'driven_wheels', 
                   'market_category', 'vehicle_size', 'vehicle_style']
print(f"Categorical variables: {categorical_vars}")

# Get the most frequent categories for each categorical variable (top 5)
print("\nIdentifying most frequent categories...")
categories = {}
for var in categorical_vars:
    # Get top 5 most frequent categories for each variable
    categories[var] = list(df[var].value_counts().head().index)
    print(f"{var}: {categories[var]}")

# Get the most popular car makes (top 5)
popular_makes = list(df.make.value_counts().head().index)
print(f"Most popular makes: {popular_makes}")

# Define a function to prepare features for the model
def prepare_X(df_input):
    """
    Prepare features for linear regression model.
    
    This function:
    1. Creates a copy of the input dataframe
    2. Adds base features
    3. Calculates car age (2017 - year)
    4. Creates dummy variables for number of doors (2, 3, 4)
    5. Creates dummy variables for popular makes
    6. Creates dummy variables for categorical variables
    7. Fills missing values with 0
    8. Returns the feature matrix as a numpy array
    
    Args:
        df_input: Input dataframe with car features
        
    Returns:
        X: Feature matrix as numpy array
    """
    df_copy = df_input.copy()  # Create a copy to avoid modifying original
    features = base_features.copy()  # Start with base features
    
    # Calculate car age (assuming data is from 2017)
    df_copy['age'] = 2017 - df_copy.year
    features.append('age')
    
    # Create dummy variables for number of doors
    for num_doors in [2, 3, 4]:
        # Create binary feature: 1 if car has this number of doors, 0 otherwise
        df_copy[f'num_doors_{num_doors}'] = (df_copy.number_of_doors == num_doors).astype('int')
        features.append(f'num_doors_{num_doors}')
    
    # Create dummy variables for popular makes
    for make in popular_makes:
        df_copy[f'make_{make}'] = (df_copy.make == make).astype('int')
        features.append(f'make_{make}')
    
    # Create dummy variables for categorical variables
    for cat_var, cat_values in categories.items():
        for value in cat_values:
            df_copy[f'{cat_var}_{value}'] = (df_copy[cat_var] == value).astype('int')
            features.append(f'{cat_var}_{value}')
    
    # Select only the prepared features
    df_numeric = df_copy[features]
    
    # Fill missing values with 0
    df_numeric = df_numeric.fillna(0)
    
    # Convert to numpy array for model training
    X = df_numeric.values
    
    return X

# Define a function to train linear regression model
def train_linear_regression(X, y):
    """
    Train a linear regression model using normal equation.
    
    This implements linear regression using the normal equation:
    w = (X^T * X)^(-1) * X^T * y
    where w is the weight vector, X is the feature matrix, and y is the target vector.
    
    The intercept (w0) is calculated separately as the mean of residuals.
    
    Args:
        X: Feature matrix (numpy array)
        y: Target vector (numpy array)
        
    Returns:
        w0: Intercept (bias term)
        w: Weight vector for features
    """
    # Add a column of ones for the intercept term
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])
    
    # Calculate weights using normal equation: w = (X^T * X)^(-1) * X^T * y
    XTX = X.T.dot(X)  # X transpose multiplied by X
    XTX_inv = np.linalg.inv(XTX)  # Inverse of XTX
    w_full = XTX_inv.dot(X.T).dot(y)  # Calculate weights
    
    # Separate intercept (w0) from feature weights (w)
    w0 = w_full[0]  # Intercept
    w = w_full[1:]  # Weights for features
    
    return w0, w

# Define a function to calculate RMSE (Root Mean Squared Error)
def rmse(y_true, y_pred):
    """
    Calculate Root Mean Squared Error.
    
    RMSE measures the average magnitude of prediction errors.
    Lower values indicate better model performance.
    
    Formula: sqrt(mean((y_true - y_pred)^2))
    
    Args:
        y_true: Actual target values
        y_pred: Predicted values
        
    Returns:
        rmse: Root Mean Squared Error
    """
    error = y_true - y_pred  # Calculate prediction errors
    se = error ** 2  # Square the errors
    mse = se.mean()  # Calculate mean squared error
    return np.sqrt(mse)  # Return square root (RMSE)

# Train the model and evaluate on validation set
print("\nTraining linear regression model...")
X_train = prepare_X(df_train)  # Prepare training features
w0, w = train_linear_regression(X_train, y_train)  # Train model

X_val = prepare_X(df_val)  # Prepare validation features
y_pred = w0 + X_val.dot(w)  # Make predictions on validation set

# Calculate RMSE on validation set
val_rmse = rmse(y_val, y_pred)
print(f"Validation RMSE: {val_rmse:.6f}")

# Visualize predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_val, y_pred, alpha=0.5)
plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--', lw=2)
plt.xlabel('Actual Log Price')
plt.ylabel('Predicted Log Price')
plt.title('Predictions vs Actual Values (Validation Set)')
plt.show()

# Convert log predictions back to original scale for interpretation
y_pred_original = np.expm1(y_pred)  # expm1(x) = exp(x) - 1
y_val_original = np.expm1(y_val)

# Show some example predictions
print("\nExample predictions (Validation Set):")
for i in range(5):
    print(f"Actual: ${y_val_original[i]:,.0f}, Predicted: ${y_pred_original[i]:,.0f}")

# Train model with regularization
def train_linear_regression_reg(X, y, r=0.001):
    """
    Train linear regression with L2 regularization (Ridge regression).
    
    Regularization helps prevent overfitting by adding a penalty term to the loss function.
    L2 regularization adds r * sum(w^2) to the loss, where r is the regularization parameter.
    
    The normal equation with regularization becomes:
    w = (X^T * X + r * I)^(-1) * X^T * y
    where I is the identity matrix (excluding intercept).
    
    Args:
        X: Feature matrix
        y: Target vector
        r: Regularization parameter (lambda)
        
    Returns:
        w0: Intercept
        w: Regularized weight vector
    """
    # Add column of ones for intercept
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])
    
    # Create identity matrix for regularization (exclude intercept)
    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])  # Identity matrix scaled by r
    reg[0, 0] = 0  # Don't regularize the intercept
    
    # Add regularization to XTX
    XTX = XTX + reg
    
    # Calculate regularized weights
    XTX_inv = np.linalg.inv(XTX)
    w_full = XTX_inv.dot(X.T).dot(y)
    
    w0 = w_full[0]
    w = w_full[1:]
    
    return w0, w

# Find optimal regularization parameter
print("\nFinding optimal regularization parameter...")
r_values = [0, 0.000001, 0.0001, 0.001, 0.01, 0.1, 1, 5, 10]
rmse_scores = []

for r in r_values:
    # Train model with regularization
    X_train_reg = prepare_X(df_train)
    w0_reg, w_reg = train_linear_regression_reg(X_train_reg, y_train, r=r)
    
    # Make predictions on validation set
    X_val_reg = prepare_X(df_val)
    y_pred_reg = w0_reg + X_val_reg.dot(w_reg)
    
    # Calculate RMSE
    score = rmse(y_val, y_pred_reg)
    rmse_scores.append(score)
    print(f"r={r}: RMSE={score:.6f}")

# Plot RMSE vs regularization parameter
plt.figure(figsize=(10, 6))
plt.plot(r_values, rmse_scores, 'bo-')
plt.xscale('log')
plt.xlabel('Regularization Parameter (r)')
plt.ylabel('RMSE')
plt.title('RMSE vs Regularization Parameter')
plt.grid(True, alpha=0.3)
plt.show()

# Find best regularization parameter
best_idx = np.argmin(rmse_scores)
best_r = r_values[best_idx]
best_rmse = rmse_scores[best_idx]

print(f"\nBest regularization parameter: r={best_r}")
print(f"Best RMSE: {best_rmse:.6f}")

# Train final model with best regularization parameter
print("\nTraining final model with optimal regularization...")
X_train_final = prepare_X(df_train)
w0_final, w_final = train_linear_regression_reg(X_train_final, y_train, r=best_r)

X_val_final = prepare_X(df_val)
y_pred_final = w0_final + X_val_final.dot(w_final)

final_rmse = rmse(y_val, y_pred_final)
print(f"Final model RMSE: {final_rmse:.6f}")

# Evaluate on test set
print("\nEvaluating final model on test set...")
X_test = prepare_X(df_test)
y_pred_test = w0_final + X_test.dot(w_final)
test_rmse = rmse(y_test, y_pred_test)
print(f"Test RMSE: {test_rmse:.6f}")

# Convert test predictions back to original scale
y_pred_test_original = np.expm1(y_pred_test)
y_test_original = np.expm1(y_test)

# Show test set predictions
print("\nTest set predictions:")
for i in range(5):
    print(f"Actual: ${y_test_original[i]:,.0f}, Predicted: ${y_pred_test_original[i]:,.0f}")

# Create a prediction function for new cars
def predict_car_price(car_features, w0=w0_final, w=w_final):
    """
    Predict price for a new car.
    
    Args:
        car_features: Dictionary or DataFrame with car features
        w0: Intercept (default: from final model)
        w: Weight vector (default: from final model)
        
    Returns:
        predicted_price: Predicted price in original scale
    """
    # If single car (dictionary), convert to DataFrame
    if isinstance(car_features, dict):
        car_df = pd.DataFrame([car_features])
    else:
        car_df = car_features.copy()
    
    # Prepare features
    X_car = prepare_X(car_df)
    
    # Make prediction (in log scale)
    y_pred_log = w0 + X_car.dot(w)
    
    # Convert back to original scale
    predicted_price = np.expm1(y_pred_log)
    
    return predicted_price

# Example: Predict price for a specific car
print("\nExample prediction for a specific car:")
example_car = {
    'make': 'chevrolet',
    'model': 'trailblazer_ext',
    'year': 2004,
    'engine_fuel_type': 'regular_unleaded',
    'engine_hp': 275.0,
    'engine_cylinders': 6.0,
    'transmission_type': 'automatic',
    'driven_wheels': 'rear_wheel_drive',
    'number_of_doors': 4.0,
    'market_category': 'crossover',
    'vehicle_size': 'large',
    'vehicle_style': '4dr_suv',
    'highway_mpg': 18,
    'city_mpg': 13,
    'popularity': 1385
}

predicted_price = predict