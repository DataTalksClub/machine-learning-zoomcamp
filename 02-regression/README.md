## 2. Machine Learning for Regression

- 2.1 [Car price prediction project](01-car-price-intro.md) - Introduce the car price project, its Kaggle dataset, the MSRP target, and the steps of the project plan.
- 2.2 [Data preparation](02-data-preparation.md) - Load the Kaggle car dataset with pandas and normalize column names and string values to lowercase with underscores.
- 2.3 [Exploratory data analysis](03-eda.md) - Explore each column, log-transform the long-tailed price distribution, and count missing values.
- 2.4 [Setting up the validation framework](04-validation-framework.md) - Split the car data into shuffled 60/20/20 train, validation, and test sets using plain pandas and NumPy.
- 2.5 [Linear regression](05-linear-regression-simple.md) - Implement a linear regression prediction for one car as a weighted sum of its features plus a bias.
- 2.6 [Linear regression: vector form](06-linear-regression-vector.md) - Rewrite linear regression as a dot product and then a matrix-vector multiplication that predicts all cars at once.
- 2.7 [Training linear regression: Normal equation](07-linear-regression-training.md) - Derive the normal equation for linear regression weights and implement it as a train_linear_regression function.
- 2.8 [Baseline model for car price prediction project](08-baseline-model.md) - Train a baseline model on five numerical features, filling missing values with zeros, and compare its predictions with actual prices.
- 2.9 [Root mean squared error](09-rmse.md) - Explain RMSE with a worked example, implement it in NumPy, and apply it to the baseline model.
- 2.10 [Using RMSE on validation data](10-car-price-validation.md) - Build a prepare_X helper and compute RMSE on the validation set instead of the training set.
- 2.11 [Feature engineering](11-feature-engineering.md) - Create an age feature from the year column, copy the dataframe in prepare_X, and check how it lowers validation RMSE.
- 2.12 [Categorical variables](12-categorical-variables.md) - Encode doors, make, and other categories as binary columns, and observe that adding them all worsens validation RMSE.
- 2.13 [Regularization](13-regularization.md) - Explain why the normal equation breaks on duplicate features and add a diagonal term to keep weights stable.
- 2.14 [Tuning the model](14-tuning-model.md) - Tune the regularization parameter on the validation set, then train the model with the chosen value.
- 2.15 [Using the model](15-using-model.md) - Train the final model on train and validation data, check its test RMSE, and predict the price of one car.
- 2.16 [Car price prediction project summary](16-summary.md) - Recap the car price project, covering data preparation, linear regression, RMSE, feature engineering, and regularization.
- 2.17 [Explore more](17-explore-more.md) - Suggest optional practice ideas, including testing 10 features and trying other regression datasets.



## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Notes from Kwang Yang](https://www.kaggle.com/kwangyangchia/notebook-for-lesson-2-mle)
* [Notes from Sebastián Ayala Ruano](https://github.com/sayalaruano/100DaysOfMLCode/blob/main/Regression/Notes/NotesDay5.md)
* [Notes from Ayoub Berdeddouch](https://github.com/ayoub-berdeddouch/mlbookcamp-homeworks/blob/main/Regression/homework_Regression_AyoubBerdeddouch.ipynb)
* [Notes from Alvaro Navas](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/02_linear_regression.md)
* [Notes from froukje](https://github.com/froukje/ml-zoomcamp/blob/main/week2/Lecture_2_car_price_prediction.ipynb)
* [Notes from Jon Areas](https://github.com/jxareas/Machine-Learning-Bookcamp-2022/blob/master/notes/02-regression.md)
* [Notes from Memoona Tahira](https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/Week_2-linear_regression/readme.md)
* [Notes from Wesley Barreto](https://github.com/wgb-10/ML-Zoomcamp-2022/blob/main/Session-Projects/02-Regression/my-notebook.ipynb)
* [Notes from Hareesh Tummala](https://github.com/tummala-hareesh/ml_zoomcamp_ht/blob/main/notes/week-2-notes.md)
* [Notes from Anneysha Sarkar](https://github.com/Anneysha7/ml-zoomcamp-2023/blob/main/course-notes/week-2.md)
* [Notes from Peter Ernicke](https://knowmledge.com/category/courses/ml-zoomcamp/regression/)
* [Notes from Marcos Benício](https://github.com/marcosbenicio/DataScience/blob/main/01Regression/car_price.ipynb)
* [Notes from Oscar Garcia](https://github.com/ozkary/machine-learning-engineering/tree/main/02-regression)
* [Notes from Maximilien Eyengue](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/02_regression/Summary_Session_02.md)
* [Notes from Kemal Dahha](https://github.com/kemaldahha/machine-learning-course/blob/main/week_2_notes.ipynb)
* [Cohort 2025 | Notes By Nitin Gupta](https://github.com/niting9881/ML-zoomcamp-local/blob/main/02-regression/Linear_Regression_FAQ.md)
* Add your notes here

