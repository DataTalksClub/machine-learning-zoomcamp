## 6. Decision Trees and Ensemble Learning

- 6.1 [Credit risk scoring project](01-credit-risk.md) - Introduce the credit risk project, where a model predicts whether a bank customer will default on a loan.
- 6.2 [Data cleaning and preparation](02-data-prep.md) - Download the credit scoring data, decode categorical codes, replace 99999999 placeholders with NaN, and split into 60/20/20 sets.
- 6.3 [Decision trees](03-decision-trees.md) - Train a scikit-learn decision tree, observe overfitting from training and validation AUC, and limit depth with max_depth.
- 6.4 [Decision tree learning algorithm](04-decision-tree-learning.md) - Walk through how a decision tree picks the lowest-impurity split on a toy dataset and when it stops splitting.
- 6.5 [Decision trees parameter tuning](05-decision-tree-tuning.md) - Tune max_depth and min_samples_leaf on validation AUC with a heatmap, then train the final tree and inspect its rules.
- 6.6 [Ensemble learning and random forest](06-random-forest.md) - Build a random forest and tune n_estimators, max_depth, and min_samples_leaf using validation AUC curves.
- 6.7 [Gradient boosting and XGBoost](07-boosting.md) - Train an XGBoost model on DMatrix data, then parse its training output to plot train and validation AUC by round.
- 6.8 [XGBoost parameter tuning](08-xgb-tuning.md) - Tune XGBoost eta, max_depth, and min_child_weight one at a time by comparing validation AUC curves.
- 6.9 [Selecting the best model](09-final-model.md) - Compare tuned decision tree, random forest, and XGBoost on validation, then retrain the best model and check test AUC.
- 6.10 [Summary](10-summary.md) - Recap decision trees, random forests, and gradient boosting, and the final XGBoost AUC on validation and test.
- 6.11 [Explore more](11-explore-more.md) - Suggest follow-up experiments such as EDA, ExtraTreesClassifier, XGBoost subsample tuning, and tree regression.


## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Kwang Yang's Notes](https://www.kaggle.com/kwangyangchia/notebook-for-lesson-6-mle)
* [Alvaro Navas' Notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/06_trees.md)
* [Notes from froukje](https://github.com/froukje/ml-zoomcamp/blob/main/week6/Lecture_6_Decision_Trees_Ensemble_Learning.ipynb)
* [Decision Trees and Ensembled Learning by Oscar Garcia](https://github.com/ozkary/machine-learning-engineering/tree/main/06-trees)
* [Notes from Peter Ernicke](https://knowmledge.com/category/courses/ml-zoomcamp/decision-trees/)
* [Notes from Maximilien Eyengue](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/06_trees/Summary_Session_06.md)
* [Notes from Kemal Dahha](https://github.com/kemaldahha/machine-learning-course/blob/main/week_6_notes.ipynb)
* Add your notes here
