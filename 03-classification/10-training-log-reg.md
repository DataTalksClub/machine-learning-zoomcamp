---
video_url: https://www.youtube.com/watch?v=hae_jXe2fN0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR
code:
  - label: Notebook
    path: notebook.ipynb
---
# Training logistic regression with Scikit-Learn

In this lesson we train a logistic regression model on the encoded
training data, apply it to the validation set, and measure how good it
is with accuracy.

## Training the model

Scikit-Learn has a ready-made implementation of logistic regression.
Training it follows the same pattern as `LinearRegression` in the
previous module: create the model, then call `fit` with the feature
matrix and the target vector.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='lbfgs')
# solver='lbfgs' is the default solver in newer version of sklearn
# for older versions, you need to specify it explicitly
model.fit(X_train, y_train)
```

The `solver` is the optimization algorithm that finds the best weights.
After `fit`, the model has learned both parts of the formula from the
previous lesson. The bias term `w0` is in `intercept_`:

```python
model.intercept_[0]
```

```
-0.10903395348323511
```

The weights are in `coef_` - one weight for each of the 45 columns that
`DictVectorizer` produced:

```python
model.coef_[0].round(3)
```

```
array([ 0.475, -0.175, -0.408, -0.03 , -0.078,  0.063, -0.089, -0.081,
       -0.034, -0.073, -0.335,  0.316, -0.089,  0.004, -0.258,  0.141,
        0.009,  0.063, -0.089, -0.081,  0.266, -0.089, -0.284, -0.231,
        0.124, -0.166,  0.058, -0.087, -0.032,  0.07 , -0.059,  0.141,
       -0.249,  0.215, -0.12 , -0.089,  0.102, -0.071, -0.089,  0.052,
        0.213, -0.089, -0.232, -0.07 ,  0.   ])
```

We will read these coefficients in the next lesson.

## Making predictions

The model has two prediction methods, and the difference matters:

- `model.predict(X)` gives hard predictions - the final 0/1 answer
- `model.predict_proba(X)` gives soft predictions - the actual
  probabilities

We want the probabilities, because we will apply our own threshold:

```python
y_pred = model.predict_proba(X_val)[:, 1]
```

`predict_proba` returns a matrix with two columns: the probability of
class 0 and the probability of class 1. The two columns always sum up
to 1, so it is enough to take the second one - hence `[:, 1]`.

Now we decide: if the model thinks the probability of churn is 50% or
more, we predict that the customer will churn:

```python
churn_decision = (y_pred >= 0.5)
```

The result is a boolean array. We can use it to select the customers
the model thinks will churn - for example, the ones who should receive
a promotional email with a discount. Selecting the validation rows with
this mask gives 311 customers.

## Accuracy

To see whether these predictions are any good, we compare them with the
actual labels of the validation set:

```python
(y_val == churn_decision).mean()
```

```
0.8034066713981547
```

This metric is accuracy: the fraction of predictions the model got
right. Here it is 80% - in 80% of the cases, the model predicted churn
or no churn correctly.

We can also look at it from a dataframe. Let's put the predictions and
the actual values side by side:

```python
df_pred = pd.DataFrame()
df_pred['probability'] = y_pred
df_pred['prediction'] = churn_decision.astype(int)
df_pred['actual'] = y_val
```

And mark the rows where the prediction matches reality:

```python
df_pred['correct'] = df_pred.prediction == df_pred.actual
df_pred.correct.mean()
```

```
0.8034066713981547
```

Same number, as expected. Taking the mean of a boolean column counts
the fraction of `True` values, because `True` is 1 and `False` is 0.

An accuracy of 80% is a reasonable start for this problem. The choice
of the 0.5 threshold affects this number - we will see how to pick a
better threshold when we look at classification metrics in more detail.

## Materials

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-3-machine-learning-for-classification)

## Notes

This video was about training a logistic regression model with Scikit-Learn, applying it to the validation dataset, and calculating its accuracy. 

**Classes, functions, and methods:** 

* `LogisticRegression().fit(x)` - Scikit-Learn class for training the logistic regression model. 
* `LogisticRegression().coef_[0]` - return the coefficients or weights of the LR model
* `LogisticRegression().intercept_[0]` - return the bias or intercept of the LR model
* `LogisticRegression().predict[x]` - make predictions on the x dataset 
* `LogisticRegression().predict_proba[x]` - make predictions on the x dataset by returning two columns with their probabilities for the two categories - soft predictions

The entire code of this project is available in [this jupyter notebook](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/03-classification/notebook.ipynb).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/30/ml-zoomcamp-2023-machine-learning-for-classification-part-10/)
