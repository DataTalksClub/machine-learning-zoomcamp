
## 2.5 Linear regression

<a href="https://www.youtube.com/watch?v=Dn1eTQLsOdA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=16"><img src="images/thumbnail-2-05.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)


## Notes

Model for solving regression tasks, in which the objective is to adjust a line for the data and make predictions on new values. The input of this model is 
the feature matrix and a y vector of predictions is obtained, trying to be as close as possible to the actual y values. The LR formula is the sum of the 
bias term (WO), which refers to the predictions if there is no information, and each of the feature values times their corresponding weights. We need to 
assure that the result is shown on the untransformed scale. 

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

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 2: Machine Learning for Regression](./)
* Previous: [Setting up the validation framework](04-validation-framework.md)
* Next: [Linear regression: vector form](06-linear-regression-vector.md)
