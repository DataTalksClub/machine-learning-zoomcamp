## Homework

### Set up the environment

You need to install Python, NumPy, Pandas, Matplotlib and Seaborn. For that, you can use the instructions from
[06-environment.md](../../../01-intro/06-environment.md).

### Q1. Pandas version

What's the version of Pandas that you installed?

You can get the version information using the `__version__` field:

```python
pd.__version__
```

### Getting the data 

For this homework, we'll use the Laptops Price dataset. Download it from 
[here](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv).

You can do it with wget:

```bash
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv
```

Or just open it with your browser and click "Save as...".

Now read it with Pandas.

### Q2. Records count

How many records are in the dataset?

- 12
- 1000
- 2160
- 12160

### Q3. Laptop brands

How many laptop brands are presented in the dataset?

- 12
- 27
- 28
- 2160

### Q4. Missing values

How many columns in the dataset have missing values?

- 0
- 1
- 2
- 3

### Q5. Maximum final price

What's the maximum final price of Dell notebooks in the dataset?

- 869
- 3691
- 3849
- 3936

### Q6. Median value of Screen

1. Find the median value of `Screen` column in the dataset.
2. Next, calculate the most frequent value of the same `Screen` column.
3. Use `fillna` method to fill the missing values in `Screen` column with the most frequent value from the previous step.
4. Now, calculate the median value of `Screen` once again.

Has it changed?

> Hint: refer to existing `mode` and `median` functions to complete the task.

- Yes
- No

### Q7. Sum of weights

1. Select all the "Innjoo" laptops from the dataset.
2. Select only columns `RAM`, `Storage`, `Screen`.
3. Get the underlying NumPy array. Let's call it `X`.
4. Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
5. Compute the inverse of `XTX`.
6. Create an array `y` with values `[1100, 1300, 800, 900, 1000, 1100]`.
7. Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
8. What's the sum of all the elements of the result?

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.

- 0.43
- 45.29
- 45.58
- 91.30


## Submit the results

* Submit your results here: https://courses.datatalks.club/ml-zoomcamp-2024/homework/hw01
* If your answer doesn't match options exactly, select the closest one. If the answer is exactly in between two options, select the higher value.
