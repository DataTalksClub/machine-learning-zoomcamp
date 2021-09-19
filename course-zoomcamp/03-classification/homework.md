## 3.15 Homework

### Dataset

In this homework, we will still use the New York City Airbnb Open Data. You can take it from
[Kaggle](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data?select=AB_NYC_2019.csv)
or download from [here](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/AB_NYC_2019.csv)
if you don't want to sign up to Kaggle.

The goal of this homework is to work with (column `'price'`), but in this homework we will work further on it and transform this variable to solve classification task.


### Features

For the rest of the homework, you'll need to use the features from the previous homework with additional two `'neighbourhood_group'` and `'room_type'`. So the whole feature set will be set as follows:

* `'neighbourhood_group'`,
* `'room_type'`,
* `'latitude'`,
* `'longitude'`,
* `'price'`,
* `'minimum_nights'`,
* `'number_of_reviews'`,
* `'reviews_per_month'`,
* `'calculated_host_listings_count'`,
* `'availability_365'`

Select only them.

### Question 1

What is the most frequent observation (mode) in a column `'neighbourhood_group'`?


### Question 2

Create the correlation matrix for the numerical features. What are the two features that have the biggest correlation in this dataset?


### Split the data

* Split your data in train/val/test sets, with 60%/20%/20% distribution.
* Make sure that the target value ('price') is not in your dataframe.


### Question 3

* Calculate mutual_info_score for two categorical variables that you have. Use train set.
* Which of these two variables has bigger mutual_info_score
* Specify this score and round it to 2 decimal digits using `round(score, 2)`

### Question 4

* Now let's train a logistic regression
* Before training, apply OneHotEncoder() to your data and transform the categorical variables.
* Fit the model on train data 
* Calculate Accutacy Score on Test data and rount it to 2 decimal digits

### Question 5

* For this question, you need to use the original column `'price'`
* Apply log transformation to `'price'`
* Fit the Ridge Regression model on train data
* Calculate RMSE on validation set using alpha = 0.5. Round result to 2 digits.


## Submit the results

Submit your results here: 

If your answer doesn't match options exactly, select the closest one.

## Deadline


The deadline for submitting is 27 September 2021, 17:00 CET. After that, the form will be closed.



## Nagivation

* [Machine Learning Zoomcamp course](../)
* [Session 3: Machine Learning for Classification](./)
* Previous: [Explore more](14-explore-more.md)
