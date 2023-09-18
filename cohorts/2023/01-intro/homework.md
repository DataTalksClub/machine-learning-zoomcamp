## Homework

### Set up the environment

You need to install Python, NumPy, Pandas, Matplotlib and Seaborn. For that, you can the instructions from
[06-environment.md](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/01-intro/06-environment.md).

### Question 1

What's the version of Pandas that you installed?

You can get the version information using the `__version__` field:

```python
pd.__version__
```

### Getting the data 

For this homework, we'll use the California Housing Prices dataset. Download it from 
[here](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv).

You can do it with wget:

```bash
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv
```

Or just open it with your browser and click "Save as...".

Now read it with Pandas.

### Question 2

How many columns are in the dataset?

- 10
- 6560
- 10989
- 20640

### Question 3

Which columns in the dataset have missing values?

- `total_rooms`
- `total_bedrooms`
- both of the above
- no empty columns in the dataset

### Question 4

How many unique values does the `ocean_proximity` column have?

- 3
- 5
- 7
- 9

### Question 5

What's the average value of the `median_house_value` for the houses located near the bay?

- 49433
- 124805
- 259212
- 380440

### Question 6

1. Calculate the average of `total_bedrooms` column in the dataset.
2. Use the `fillna` method to fill the missing values in `total_bedrooms` with the mean value from the previous step.
3. Now, calculate the average of `total_bedrooms` again.
4. Has it changed?

Has it changed?

> Hint: take into account only 3 digits after the decimal point.

- Yes
- No

### Question 7

1. Select all the options located on islands.
2. Select only columns `housing_median_age`, `total_rooms`, `total_bedrooms`.
3. Get the underlying NumPy array. Let's call it `X`.
4. Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
5. Compute the inverse of `XTX`.
6. Create an array `y` with values `[950, 1300, 800, 1000, 1300]`.
7. Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
8. What's the value of the last element of `w`?

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.

- -1.4812
- 0.001
- 5.6992
- 23.1233


## Submit the results

* Submit your results here: https://forms.gle/jneGM91mzDZ23i8HA
* You can submit your solution multiple times. In this case, only the last submission will be used 
* If your answer doesn't match options exactly, select the closest one


## Deadline

The deadline for submitting is 18 September 2023 (Monday), 23:00 CEST (Berlin time).

After that, the form will be closed.

