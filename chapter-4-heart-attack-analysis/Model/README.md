# **Heart Attack Analysis **


**GOAL**

- The goal of this exercise is to identify the parameters that influences the heart attack and build a ML model for the prediction of heart attack.


**DATASET**

Dataset can be downloaded from [here](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset).



**WHAT I HAD DONE**

- Importing Libraries
- Missing Value Analysis
- Categoric and Numeric Features
- Standardization
- Box - Swarm - Cat - Correlation Plot Analysis
- Outlier Detection
- Machine Learning Model


**MODELS USED**

-  Logistic Regression
-  Linear SVC
-  Support Vector Machines
-  Random Forest
-  KNN
-  Stochastic Gradient Decentt
-  Decision Tree
-  Gaussian Naive Bayes


**LIBRARIES NEEDED**

- numpy
- pandas
- seaborn
- matplotlib
- scipy.stats
- scikit-learn

**Accuracy of different models used**

By using Logistic Regression I got 
 ```python
    test accuracy score of  Logistic Regression =  93.42105263157895
 ``` 

By using Random Forest Classifier I got 
 ```python
    test accuracy score of Random Forest =  86.8421052631579
 ``` 
 
 By using Decision Tree Classifier I got 
 ```python
    test accuracy score of Decision Tree =  81.57894736842105
 ``` 
 
  By using  Support Vector Machine I got 
 ```python
    test accuracy score of Support Vector Machine =  90.78947368421053
 ``` 
 
  By using  Stochastic Gradient Descentt I got 
 ```python
    test accuracy score of Stochastic Gradient Descentt =  82.89473684210526
 ``` 
 
  By using Linear SVC I got 
 ```python
    test accuracy score of  Linear SVC =  90.78947368421053
 ``` 
 
  By using KNN I got 
 ```python
    test accuracy score of KNN =  85.52631578947368
 ``` 
 
  By using Gaussian Naive Bayes I got 
 ```python
    test accuracy score of Gaussian Naive Bayes =  77.63157894736842
 ``` 
 
 
 **CONCLUSION**
 
- Most of the models are working brilliantly on this dataset after normalising the dataset.
- Performance of **Logistic regression** is better in terms of accuracy as compared to other model.
- Only looking at accuracy as evaluation metrics in this case might be deadly as we need to look for **False Negative**.
- Hence , we are looking at complete classification report , especisally **Recall**



### BY :  Harshita Nayak
