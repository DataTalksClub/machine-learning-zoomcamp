## 6. Decision Trees and Ensemble Learning

- 6.1 [Credit risk scoring project](01-credit-risk.md)
- 6.2 [Data cleaning and preparation](02-data-prep.md)
- 6.3 [Decision trees](03-decision-trees.md)
- 6.4 [Decision tree learning algorithm](04-decision-tree-learning.md)
- 6.5 [Decision trees parameter tuning](05-decision-tree-tuning.md)
- 6.6 [Ensemble learning and random forest](06-random-forest.md)
- 6.7 [Gradient boosting and XGBoost](07-boosting.md)
- 6.8 [XGBoost parameter tuning](08-xgb-tuning.md)
- 6.9 [Selecting the best model](09-final-model.md)
- 6.10 [Summary](10-summary.md)
- 6.11 [Explore more](11-explore-more.md)
- 6.12 [Homework](homework.md)


## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Kwang Yang's Notes] (https://www.kaggle.com/kwangyangchia/notebook-for-lesson-6-mle)
* Add your notes here

## Mac XGBoost install and hang workaround

When you run `pip install xgboost` or when you try to `import xgboost` in a script you might get an warning or error stating that libomp has not been installed and to run `brew install libomp` in the terminal. However this install a version of libomp that does not work with `xgboost`!

This shows in one of two ways after attempting to run `xgb.DMatrix(X_train, label=y_train, feature_names=features)`:

- **python script:** Segmentation fault: 11
- **jupyter notebook:** Never finished running, and notebook is unresponsive until kernal restart. However confusingly it sometimes works

The versions of libomp with this problem are 12.x.x and 13.x.x, however issue has a workaround [xgboost issue #7039](https://github.com/dmlc/xgboost/issues/7039) installing the older libomp 11 using the terminal. In the terminal run `brew list --version libomp`, to determine the current version of libomp if any. Then if you have a problematic version run `brew unlink libomp`.
Now to install the old version of libomp run:
```
brew update
wget https://raw.githubusercontent.com/chenrui333/homebrew-core/0094d1513ce9e2e85e07443b8b5930ad298aad91/Formula/libomp.rb
brew install --build-from-source ./libomp.rb
```
and then run 
```brew list --version libomp```
to check that everything worked, it should now state `libomp 11.1.0`, and your code should now be able to run.
