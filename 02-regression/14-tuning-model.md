---
video_url: https://www.youtube.com/watch?v=lW-YVxPgzQw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=25
code:
  - label: Notebook
    path: notebook.ipynb
---
# Tuning the model

In the [previous unit](13-regularization.md) we saw that the regularization
parameter `r` affects the quality of our model. Tuning the model means finding
the best value for this parameter - and the validation set is exactly the tool
for that.

## Trying different values of r

What we will do is simply try a bunch of different values for `r`: starting from
zero, then something small, gradually increasing it, and maybe even 10:

```python
for r in [0.0, 0.00001, 0.0001, 0.001, 0.1, 1, 10]:
    X_train = prepare_X(df_train)
    w0, w = train_linear_regression_reg(X_train, y_train, r=r)

    X_val = prepare_X(df_val)
    y_pred = w0 + X_val.dot(w)
    score = rmse(y_val, y_pred)

    print(r, w0, score)
```

We go through this list, and for every `r` we train the model and compute the
RMSE on the validation data. For each value we print the regularization
parameter itself, the bias term, and the score:


## Reading the results


What we see: for zero regularization the bias term is huge and the RMSE is huge
too - 266. That is the broken model with the duplicated columns problem. But for
even a little bit of regularization it improves immediately, and after that the
score doesn't really change that much. It starts to become a bit worse as we
increase the regularization, and when it's 10 it's even worse.

Looking at the bias term, the more regularization we add, the smaller it is. It
looks like maybe 0.001 is a good value, because the model hasn't started to
degrade in performance there, and it's not too large. To be honest, it doesn't
really matter here - it could be this one or the one next to it. We can just go
with 0.001.


## Training the final model

Let's train our model once again with the selected value:

```python
r = 0.001
X_train = prepare_X(df_train)
w0, w = train_linear_regression_reg(X_train, y_train, r=r)

X_val = prepare_X(df_val)
y_pred = w0 + X_val.dot(w)
score = rmse(y_val, y_pred)
score
```


We selected the best regularization parameter, trained the model with it, and we
saw that it works on the validation set:

```
0.46081585838957173
```

Now what we need to do is check it on the test dataset as well - and this is
what we will do in the [next unit](15-using-model.md).

## Materials

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)

## Notes

Tuning the model consisted of finding the best regularization hyperparameter value, using the validation partition of the dataset. The model was then trained with this regularization value. 

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb). 

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/24/ml-zoomcamp-2023-machine-learning-for-regression-part-12/)
