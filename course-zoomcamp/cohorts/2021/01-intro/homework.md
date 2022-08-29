## Session #1 Homework

> **Solution**: [homework-1.ipynb](homework-1.ipynb).

### Set up the environment

You need to install Python, NumPy, Pandas, Matplotlib and Seaborn. For that, you can the instructions from [06-environment.md](06-environment.md).

### Question 1

What's the version of NumPy that you installed? 

You can get the version information using the `__version__` field:

```python
np.__version__
```

### Question 2

What's the version of Pandas? 


### Getting the data 

For this homework, we'll use the same dataset as for the next session - the car price dataset.

Download it from [here](https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv).

You can do it with wget:

```bash
wget https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv
```

Or just open it with your browser and click "Save as...".

Now read it with Pandas. 


### Question 3

What's the average price of BMW cars in the dataset?


### Question 4

Select a subset of cars after year 2015 (inclusive, i.e. 2015 and after). How many of them have missing values for Engine HP?


### Question 5

* Calculate the average "Engine HP" in the dataset. 
* Use the `fillna` method and to fill the missing values in "Engine HP" with the mean value from the previous step. 
* Now, calcualte the average of "Engine HP" again.
* Has it changed? 

Round both means before answering this questions. You can use the `round` function for that:

```python
print(round(mean_hp_before))
print(round(mean_hp_after))
```


### Question 6

* Select all the "Rolls-Royce" cars from the dataset.
* Select only columns "Engine HP", "Engine Cylinders", "highway MPG".
* Now drop all duplicated rows using `drop_duplicates` method (you should get a dataframe with 7 rows).
* Get the underlying NumPy array. Let's call it `X`.
* Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
* Invert `XTX`.
* What's the sum of all the elements of the result?

Hint: if the result is negative, re-read the task one more time


### Questions 7 

* Create an array `y` with values `[1000, 1100, 900, 1200, 1000, 850, 1300]`.
* Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
* What's the value of the first element of `w`?.

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.


## Submit the results

Submit your results here: https://forms.gle/aiunQqRtqcay8Wwo9.

If your answer doesn't match options exactly, select the closest one.


## Deadline

The deadline for submitting is 13 September 2021, 17:00 CET. After that, the form will be closed.


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Lesson 1: Introduction to Machine Learning](./)
* Previous: [Summary](10-summary.md)
