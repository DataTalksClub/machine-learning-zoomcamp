## 6.6 Ensemble learning and random forest

<a href="https://www.youtube.com/watch?v=FZhcmOfNNZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-6-06.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-6-decision-trees-and-ensemble-learning)


## Notes
**Ensemble learning** is a machine learning paradigm where multiple models, often referred to as 'weak learners', are strategically combined to solve a particular computational intelligence problem. This approach frequently yields superior predictive performance compared to using a single model.

**Random Forest** is an example of ensemble learning where each model is a decision tree and their predictions are aggregated to identify the most popular result. Random forest only selects a random subset of features from the original data to make predictions. The 'randomness' in Random Forest stems from two key aspects: 

- Each tree is potentially trained on a bootstrapped sample of the original data, introducing randomness at the row level.
- At each node during tree construction, only a random subset of features is considered for splitting. This feature randomness helps decorrelate the trees, preventing overfitting and promoting generalization to unseen data.

**Bootstrapping** is a resampling technique where numerous subsets
of the data are created by sampling the original data with replacement. This means that
some data points may appear multiple times in a single bootstrap sample, while others may
be excluded. In Random Forest, each decision tree is trained on a distinct bootstrap sample,
further contributing to the diversity and robustness of the ensemble.

**Parameter tuning** is crucial for optimizing the performance of a
Random Forest model.  Two critical parameters are `max_depth`, which controls the maximum
depth of each decision tree, and `n_estimators`, which determines the number of trees in
the forest. Increasing `max_depth` allows for more complex trees, potentially leading to
overfitting. Conversely, a larger `n_estimators` generally improves model accuracy but
increases computational cost.

In random forests, the decision trees are trained independently to each other.

**Classes, functions, and methods**:

- `from sklearn.ensemble import RandomForestClassifier`: random forest classifier from sklearn ensemble class.
- `plt.plot(x, y)`: draw line plot for the values of y against x values.

Add notes from the video (PRs are welcome)

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/24/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-9/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 6: Decision Trees and Ensemble Learning](./)
* Previous: [Decision trees parameter tuning](05-decision-tree-tuning.md)
* Next: [Gradient boosting and XGBoost](07-boosting.md)
