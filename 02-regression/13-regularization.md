---
video_url: https://www.youtube.com/watch?v=91ve3EJlHBc&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=24
code:
  - label: Notebook
    path: notebook.ipynb
---
# Regularization

In the [previous unit](12-categorical-variables.md) we added categorical
variables to our model and ended up with an RMSE of 41 and huge weights. In this
unit we look at why that happened and learn a technique for dealing with it:
regularization.

## The inverse that doesn't always exist

Remember the formula for the normal equation we use for training our model:

```
w = (XᵀX)⁻¹ Xᵀ y
```

The problem we have is with this part: we need to take the inverse of the Gram
matrix `XᵀX`, and sometimes this inverse doesn't exist.

It usually happens when the feature matrix X has duplicate columns. Let's
quickly check it with a small matrix where the second and the third columns have
the same values:

```python
X = [
    [4, 4, 4],
    [3, 5, 5],
    [5, 1, 1],
    [5, 4, 4],
    [7, 5, 5],
    [4, 5, 5],
]
```

When we compute the Gram matrix, we see that it also has duplicate columns - the
second and the third are the same:


When something like that happens, the inverse simply doesn't exist. In linear
algebra they say that one column is a linear combination of the other columns -
which here just means that the third column is a duplicate of the second one.

## Noisy data makes the inverse huge

This is not exactly the case for our car price problem - there we didn't see the
singular matrix error. The reason is that real data is usually not super clean.
When people record observations, they make mistakes: instead of writing 5, they
write 5.00000001.

Let's add a tiny number like that to one value in our matrix:

```python
X = [
    [4, 4, 4],
    [3, 5, 5],
    [5, 1, 1],
    [5, 4, 4],
    [7, 5, 5],
    [4, 5, 5.00000001],
]
```

Now the columns are no longer exactly the same - they are slightly different -
so the matrix is not exactly singular anymore. It becomes at least numerically
invertible, and NumPy finds an inverse. But look at what it comes up with: the
numbers in the inverse are huge, around 10 to the power of 14.


When we use this inverse to compute the weights, the weights for the duplicated
features turn out to be very large numbers too. The weight for the unique first
feature is fine - 0.62 - but for the second and third features we get something
like 3.4 million and -3.4 million.


So whenever we have duplicates - or near-duplicates - in our feature matrix, we
get this problem.

## A smaller example

Let's illustrate all of this on a smaller matrix. This one also has a column
that is a duplicate of another one:

```python
XTX = [
    [1, 2, 2],
    [2, 1, 1],
    [2, 1, 1],
]
```

If we try to invert it, NumPy refuses: it complains that the matrix is singular
and it cannot compute the inverse:


Now let's do the same trick as before and add a tiny bit of noise:

```python
XTX = [
    [1, 2, 2],
    [2, 1, 1.0000001],
    [2, 1.0000001, 1],
]
```

The inverse exists now, but look at the numbers in it - around 5 million. We
will fix that in a second.

## Controlling the weights with regularization

To solve this problem, we can add a small number to the diagonal of the matrix.
If we add a small number to the diagonal - say 0.01 - the inverse can still be
found, and the numbers in it are much more under control. The larger the number
we add to the diagonal, the more control we get over the weights.

This works because by adding something to the diagonal, we make sure that it is
less possible that one column is a duplicate of another.

To add a number to the diagonal, we use the identity matrix - `np.eye(3)` is the
3×3 identity matrix, which has ones on the diagonal. When we add it to our
matrix, the diagonal increases by one:

```python
XTX + np.eye(3)
```


To add only a small number, we multiply the identity matrix by that number first:

```python
XTX = XTX + 0.01 * np.eye(3)
```

This way of controlling the weights is called regularization - the name comes
from controlling, regulating the weights so that they don't grow too much.

The number we add is actually a parameter. The larger the number on the
diagonal, the smaller the values in the inverse of `XᵀX`. How much regularization
to add becomes a parameter of our model.

## The regularized training function

With that, we can go back to our function for training linear regression and
slightly change it. We'll call it `train_linear_regression_reg`, and it gets one
more parameter - `r`, short for regularization:

```python
def train_linear_regression_reg(X, y, r=0.001):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    XTX = XTX + r * np.eye(XTX.shape[0])

    XTX_inv = np.linalg.inv(XTX)
    w_full = XTX_inv.dot(X.T).dot(y)

    return w_full[0], w_full[1:]
```

Everything stays the same except one line: after computing the Gram matrix, we
add `r` to the main diagonal.


Let's take the code from the previous unit and replace the training function
with this new one, using `r=0.01`:

```python
X_train = prepare_X(df_train)
w0, w = train_linear_regression_reg(X_train, y_train, r=0.01)

X_val = prepare_X(df_val)
y_pred = w0 + X_val.dot(w)
rmse(y_val, y_pred)
```

The result is not only much better than the 41 we got with the
non-regularized version - it is also better than what we had before adding all
the categorical variables:

```
0.4608208286209523
```


By adding a number to the diagonal we were able to control our weights and
regularize the model. But `r` is a parameter: if we set it too high, the model
becomes worse, and if we set it to 0, we are back to the usual linear
regression. So now we need to find the best value for `r` - and this is what we
will do in the [next unit](14-tuning-model.md).

## Notes

If the feature matrix has duplicate columns (or columns that can be expressed as a linear combination of other columns), it will not have an inverse matrix. But, sometimes this error could be passed if certain values are slightly different
between duplicated columns. 

So, if we apply the normal equation with this feature matrix, the values associated with duplicated columns are very large, which decreases
the model performance. To solve this issue, one alternative is adding a small number to the diagonal of the feature matrix, which corresponds to regularization. 

This technique 
works because the addition of small values to the diagonal makes it less likely to have duplicated columns. The regularization value is a hyperparameter of the model. After applying 
regularization the model performance improved. 

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb).  

## Comments
### Linear combination

I mentioned the term *linear combination* in the video, but didn't explain what it means. 
So if you're interested what it means, you can read here

* One column is a linear combination of others when you can express one column of a matrix as a sum of others columns
* The simplest example is when a column is an exact duplicate of another column
* Another example. Let's say we have 3 columns: `a`, `b`, `c`. If `c = 0.2 * a + 0.5 * b`, then `c` is a linear combination of `a` and `b`
* More formal definition: https://en.wikipedia.org/wiki/Linear_combination

### Ridge Regression
The regularization technique used (adding a factor to the diagonals of Gram Matrix) in this lesson is Ridge Regression. Further explanations are available in this [DataTalks.Club article](https://datatalks.club/blog/regularization-in-regression.html).
