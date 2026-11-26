## 3. Machine Learning for Classification

- 3.1 [Churn prediction project](01-churn-project.md) - Introduce the churn prediction problem as binary classification, using the Telco customer dataset.
- 3.2 [Data preparation](02-data-preparation.md) - Load the Telco churn data, normalize names and values, convert totalcharges to numbers, and encode churn as 0 or 1.
- 3.3 [Setting up the validation framework](03-validation.md) - Split the churn data into 60/20/20 train, validation, and test sets with scikit-learn, and separate the target.
- 3.4 [EDA](04-eda.md) - Check missing values, the churn rate, and the numerical and categorical columns of the full training set.
- 3.5 [Feature importance: Churn rate and risk ratio](05-risk.md) - Compare churn rates across categories using differences and risk ratios to judge which categorical features matter.
- 3.6 [Feature importance: Mutual information](06-mutual-info.md) - Measure each categorical feature's importance with mutual information and rank the features against churn.
- 3.7 [Feature importance: Correlation](07-correlation.md) - Rank numerical churn features by absolute Pearson correlation and check churn rates across tenure and charge groups.
- 3.8 [One-hot encoding](08-ohe.md) - Encode categorical churn features as one-hot columns with DictVectorizer, fitting on train and transforming validation.
- 3.9 [Logistic regression](09-logistic-regression.md) - Explain how logistic regression applies a sigmoid to a linear score, and implement the sigmoid and model in Python.
- 3.10 [Training logistic regression with Scikit-Learn](10-training-log-reg.md) - Train a scikit-learn LogisticRegression on encoded data and measure validation accuracy at a 0.5 threshold.
- 3.11 [Model interpretation](11-log-reg-interpretation.md) - Pair logistic regression weights with feature names, then train a three-feature model and score a customer by hand.
- 3.12 [Using the model](12-using-log-reg.md) - Retrain on train and validation data, check test accuracy, and score one customer's churn probability.
- 3.13 [Summary](13-summary.md) - Recap the churn project, covering data preparation, feature importance, one-hot encoding, logistic regression, and interpretation.
- 3.14 [Explore more](14-explore-more.md) - Suggest ways to extend the churn project with scikit-learn Ridge, OneHotEncoder, and StandardScaler, plus other datasets.



## Community notes

Did you take notes? You can share them here (or in each unit separately)
* [Notes from Kwang Yang](https://www.kaggle.com/kwangyangchia/notebook-for-lesson-3-mle)
* [Notes from Jaime Hipólito Cabrera](https://github.com/jaimeh94/ml-zoomcamp/blob/main/03-classification/classnotes_session03-classification.ipynb)
* [Notes from Sebastián Ayala Ruano](https://github.com/sayalaruano/100DaysOfMLCode/blob/main/Classification/Notes/NotesDay11.md)
* [Notes from Nikhil Shrestha](https://www.kaggle.com/snikhil17/chapter-3-ml-for-classification-mlzoomcamp)
* [Default of Credit Card Clients (Additional Project) from Nikhil Shrestha](https://www.kaggle.com/snikhil17/default-of-credit-card-clients-logistic-regression)
* [Notes from Alvaro Navas](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/03_classification.md)
* [Notes from froukje](https://github.com/froukje/ml-zoomcamp/blob/main/week3/Lecture_3_churn_prediction.ipynb)
* [Notes from Hareesh Tummala](https://github.com/tummala-hareesh/ml_zoomcamp_ht/blob/main/notes/week-3-notes.md)
* [Notes from Giorgos Verikios](https://github.com/g-verikios/ml_zoomcamp/blob/d412072625964385023d7100cad342ef2742659d/Classification-Churn.ipynb)
* [Notes from Memoona Tahira](https://github.com/MemoonaTahira/MLZoomcamp2022/tree/main/Notes/Week_3-logistic_regression_classification)
* [Notes from Marcos Benício](https://github.com/marcosbenicio/DataScience/blob/main/02Classification/churn.ipynb)
* [Notes from Oscar Garcia](https://github.com/ozkary/machine-learning-engineering/tree/main/03-classification)
* [Notes from Peter Ernicke](https://knowmledge.com/category/courses/ml-zoomcamp/classification/)
* [Notes from Kemal Dahha](https://github.com/kemaldahha/machine-learning-course/blob/main/week_3_notes.ipynb)
* [Notes from Maximilien Eyengue](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/03_classification/Summary_Session_03.md)
* [Cohort|2025 Notes BY Nitin Gupta](https://github.com/niting9881/ML-zoomcamp-local/blob/main/03-classification/README.md)
* Add your notes here
