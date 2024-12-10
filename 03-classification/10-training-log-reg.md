
## 3.10 Training logistic regression with Scikit-Learn

<a href="https://www.youtube.com/watch?v=hae_jXe2fN0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-3-10.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-3-machine-learning-for-classification)


## Notes

This video was about training a logistic regression model with Scikit-Learn, applying it to the validation dataset, and calculating its accuracy. 

**Classes, functions, and methods:** 

* `LogisticRegression().fit(x)` - Scikit-Learn class for training the logistic regression model. 
* `LogisticRegression().coef_[0]` - return the coefficients or weights of the LR model
* `LogisticRegression().intercept_[0]` - return the bias or intercept of the LR model
* `LogisticRegression().predict[x]` - make predictions on the x dataset 
* `LogisticRegression().predict_proba[x]` - make predictions on the x dataset by returning two columns with their probabilities for the two categories - soft predictions 

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-03-churn-prediction/03-churn.ipynb).

## Notes on the solver parameter of LogisticRegression in scikit-learn
A solver refers to the optimization algorithm used to find the coefficients (or weights) that minimize the loss. Solvers are responsible for adjusting the model's parameters during training to fit the data as well as possible.

Here are the main solvers :
1. lbfgs (Limited-memory Broyden–Fletcher–Goldfarb–Shanno)

    Type: Quasi-Newton method.
    Use case: Good for small to medium datasets, handles multinomial loss (for multiclass classification).
    Pros: Efficient for problems with large numbers of classes.
    Cons: May struggle with very large datasets.

2. liblinear

    Type: Coordinate descent algorithm.
    Use case: Useful for small to medium datasets; it works well with binary classification and supports L1 and L2 regularization.
    Pros: Suitable for smaller datasets and simpler models.
    Cons: Does not handle multinomial classification directly (one-vs-rest is used instead).

3. saga (Stochastic Average Gradient Descent)

    Type: Variation of stochastic gradient descent (SGD).
    Use case: Best for large datasets, sparse data, and models with L1 (lasso) regularization.
    Pros: Works well with large datasets, supports L1, L2, and elastic-net regularization.
    Cons: Typically slower than liblinear on smaller datasets.

4. newton-cg (Newton’s Conjugate Gradient)

    Type: Newton’s method with conjugate gradient optimization.
    Use case: Suitable for large datasets and multinomial loss.
    Pros: Can handle large datasets and problems with many classes.
    Cons: More computationally expensive than lbfgs and saga.

5. sag (Stochastic Average Gradient)

    Type: Stochastic gradient descent (SGD).
    Use case: Suitable for large datasets and models with L2 regularization.
    Pros: Fast on large datasets.
    Cons: Only supports L2 regularization.

How to Choose a Solver:

    If you’re working with a large dataset, try saga or sag.
    If you need multiclass classification, lbfgs, saga, or newton-cg are good choices.
    For small datasets, liblinear is often sufficient.
    If you need L1 regularization or sparse data, saga is recommended.



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

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 3: Machine Learning for Classification](./)
* Previous: [Logistic regression](09-logistic-regression.md)
* Next: [Model interpretation](11-log-reg-interpretation.md)
