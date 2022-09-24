
## 3.7 Feature importance: Correlation

<a href="https://www.youtube.com/watch?v=mz1707QVxiY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-3-07.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-3-machine-learning-for-classification)


## Notes

**Correlation coefficient** measures the degree of dependency between two variables. This value is negative if one variable grows while the other decreases, and it is positive if both variables increase. Depending on its size, the dependency between both variables could be low, moderate, or strong. It allows measuring the importance of numerical variables. 

If `r` is correlation coefficient, then the correlation between two variables is:

- LOW (Rarely) when  `r` is between [0, -0.2] or [0, 0.2]
- MEDIUM (Moderate) when  `r` is between [-0.2, -0.5] or [2, 0.5]
- STRONG (Often/Always) when  `r` is between [-0.5, -1.0] or [0.5, 1.0]

For churn, 
* $y \in$ {0,1}
* $x \in \mathbb{R}$

* When `r` is positive, when x increases y increases with it.
* When `r` is negative, when x increases, y decreases.
* When `r` is 0, when x increases, y does not change.

**Functions and methods:** 

* `df[x].corrwith(y)` - returns the correlation between x and y series. 

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-03-churn-prediction/03-churn.ipynb).

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
* [Session 3: Machine Learning for Classification](./)
* Previous: [Feature importance: Mutual information](06-mutual-info.md)
* Next: [One-hot encoding](08-ohe.md)
