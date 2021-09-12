
## 2.18 Homework

### Dataset

You will work in this homework with New York City Airbnb Open Data and can take it from [here](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data?select=AB_NYC_2019.csv)

The goal of this dataset is to create regression model for prediction apartment prices (feature 'price').

### Features

You need to use only the following columns from these dataset for completing the questions:

* 'latitude',
* 'longitude',
* 'price',
* 'minimum_nights',
* 'number_of_reviews',
* 'reviews_per_month',
* 'calculated_host_listings_count',
* 'availability_365'

### Descriptive Statistics

### Question 1

Name the feature that has missing values. How many missing values does it have? Fill the missings in this feature with 0 values.

### Question 2

What's the median (50% percentile) for variable 'minimum_nights'?

### Question 3

What's the maximum value for 'price' feature?

### Regression

Before starting this part, make sure that you completed next steps:

* Split your data in train-val-test sets
* The split should be organized as 60%-20%-20%
* Make sure that your y_value ('price') is not in X_features (not to overfit the model)
* Log-transform y_value (use np.log1p() function)

### Question 4

Calculate RMSE (Root Mean Squared Error) for test set of data. 


### Question 5

Imagine you have the following r (regularization parameter):

{0.000001, 0.0001, 0.001, 0.01, 0.1, 1, 5, 10}

What regularization parameter associated with min RMSE value for validation set?


## Notes

Add notes from the video (PRs are welcome)


## Nagivation

* [Machine Learning Zoomcamp course](../)
* [Session 2: Machine Learning for Regression](./)
* Previous: [Explore more](17-explore-more.md)
