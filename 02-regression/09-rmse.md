---
video_url: "https://www.youtube.com/watch?v=0LWoFtbzNUM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=20"
code:
  - label: "notebook.ipynb"
    path: "notebook.ipynb"
---
# Root Mean Squared Error (RMSE)

In the previous unit we trained our first model and plotted the
predictions against the actual values. The histograms showed the
predictions are a bit off, but a chart is not an objective measure. In
this unit we learn one way of quantifying how good or bad a regression
model is: root mean squared error, or RMSE.

## The formula

RMSE starts from the difference between the prediction and the actual
value. For each observation `i`, `g(xi)` is the prediction we make and
`yi` is the actual value. We take the difference, square it, average
these squared differences over all `m` observations, and finally take
the square root:

```text
RMSE = sqrt( (1/m) · Σ (g(xi) - yi)² )
```

Let's unpack each part with a small example.

## A worked example

Imagine we have four observations. These are our predictions, and
these are the actual prices:

```text
y_pred:  10     9     11    10
y:        9     9     10.5  11.5
```

The first step is to take the difference between each prediction and
the corresponding actual value:

```text
10 - 9    =  1
 9 - 9    =  0
11 - 10.5 =  0.5
10 - 11.5 = -1.5
```

Next, we square each difference:

```text
1   → 1
0   → 0
0.5 → 0.25
-1.5 → 2.25
```

Squaring does two things: it makes negative and positive errors
comparable - otherwise they would cancel each other out - and it
penalizes larger errors more.

Then we take the average of the squared errors:

```text
(1 + 0 + 0.25 + 2.25) / 4 = 0.875
```

This is the mean squared error, MSE. For our example, the mean squared
error is 0.875:

The last step is the square root:

```text
sqrt(0.875) ≈ 0.93
```

The square root brings the error back to the same units as the target
variable. For these four observations, 0.93 is the root mean squared
error.

## Implementation

Now let's implement this in NumPy. The function takes the vector of
actual values and the vector of predictions:

```python
def rmse(y, y_pred):
    error = y - y_pred
    se = error ** 2
    mse = se.mean()
    return np.sqrt(mse)
```

First we compute the error - the difference between `y` and `y_pred`.
Then we square it. To get the mean we don't need to sum and divide by
the number of elements: NumPy has the `mean` method, which gives us the
mean squared error directly. Finally, we take the square root and
return the result.

We can simplify the function a little by squaring the difference
inline:

```python
def rmse(y, y_pred):
    se = (y - y_pred) ** 2
    mse = se.mean()
    return np.sqrt(mse)
```

Now let's use it to evaluate our baseline model. We already have the
predictions `y_pred` on the training set:

```python
rmse(y_train, y_pred)
```

```text
0.7554192603920132
```


The RMSE of the baseline model is about 0.76. This single number is
much easier to work with than a chart: whenever we change something -
add a feature, transform a variable, try a different model - we
recompute it. If the number goes down, the model got better.

So far we computed it on the training data. In the next unit we apply
the model to the validation set and see how it performs there.

## Notes

* In the previous lesson we found out our predictions were a bit off from the actual target values in the training dataset. We need a way to quantify how good or bad the model is. This is where RMSE can be of help.
* Root Mean Squared Error (RMSE) is a way to evaluate regression models. It measures the error associated with the model being evaluated. This numerical figure can then be used to compare models, enabling us to choose the one that gives the best predictions.

$$RMSE = \sqrt{ \frac{1}{m} \sum_{i=1}^{m} {(g(x_i) - y_i)^2}}$$

- $g(x_i)$ is the prediction
- $y_i$ is the actual value
- $m$ is the number of observations in the dataset (i.e. cars)


The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb). 
