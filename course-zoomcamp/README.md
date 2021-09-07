# Machine Learning Zoomcamp

<a href="https://www.youtube.com/watch?v=rowoDjPc8HU"><img src="https://datatalks.club/images/courses/zoomcamp.jpg" /></a>

[Course overview video](https://www.youtube.com/watch?v=rowoDjPc8HU) and [slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-course-overview-and-logistics)

[Register for the course here](https://airtable.com/shr6Gz46UZCgJ9l6w)

[Public calendar](https://calendar.google.com/calendar/?cid=cGtjZ2tkbGc1OG9yb2lxa2Vwc2g4YXMzMmNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) (subscribing works from desktop only)


## 1. [Introduction to Machine Learning](01-intro/)

- 1.1 [Introduction to Machine Learning](01-intro/01-what-is-ml.md)
- 1.2 [ML vs Rule-Based Systems](01-intro/02-ml-vs-rules.md)
- 1.3 [Supervised Machine Learning](01-intro/03-supervised-ml.md)
- 1.4 [CRISP-DM](01-intro/04-crisp-dm.md)
- 1.5 [Model Selection Process](01-intro/05-model-selection.md)
- 1.6 [Setting up the Environment](01-intro/06-environment.md)
- 1.7 [Introduction to NumPy](01-intro/07-numpy.md)
- 1.8 [Linear Algebra Refresher](01-intro/08-linear-algebra.md)
- 1.9 [Introduction to Pandas](01-intro/09-pandas.md)
- 1.10 [Summary](01-intro/10-summary.md)
- 1.11 [Homework](01-intro/homework.md)

## 2. Machine Learning for Regression

- 2.1 Car price prediction project
- 2.2 EDA
- 2.3 Setting up the validation framework
- 2.4 Linear regression
- 2.5 Applying linear regression
- 2.6 Linear regression: matrix form
- 2.7 Training linear regression: Normal equation
- 2.8 Implementing linear regression with NumPy
- 2.9 Car price - the baseline solution
- 2.10 Evaluating the model with RMSE
- 2.11 Validating the model
- 2.12 Feature engineering
- 2.13 Categorical variables
- 2.14 Regularization
- 2.15 Tuning the model
- 2.16 Using the model
- 2.17 Car price prediction project summary
- 2.18 explore more
- 2.19 homework

## 3. Machine Learning for Classification

- Churn prediction project
- Initial data preparation
- Setting up the validation framework
- EDA
- Feature importance: Churn rate
- Feature importance: Risk ratio
- Feature importance: Mutual information
- Feature importance: Correlation
- One-hot Encoding
- Logistic regression
- Logistic regression with sklearn
- Using logistic regression (?)
- Logistic regression - interpretation
- Applying logistic regression
- Summary
- Explore more
- Homework

## 4. Evaluation Metrics for Classification

- Evaluation metrics
- Accuracy
- Baseline solution
- Confusion table
- Calculating the confusion table
- Precision and recall
- Receiver operating characteristic (ROC)
- ROC: Random baseline
- ROC: Ideal model
- The ROC Curve
- ROC curve with skilearn
- Area under the ROC Curve (AUC)
- intepretation of AUC
- K-fold cross-validation
- Selecting the best parameter C
- summary
- explore more
- homework

## 5. Deploying Machine Learning Models

- Using the model
- pickle
- Deploying a model as a Web Service
- Introduction to Flask
- Model serving with flask
- Managing dependencies with Pipenv
- Introduction to Docker
- Testing it locally
- AWS beanstalk
- summary
- explore more
- homework

## 6. Decision Trees and Ensemble Learning

- Credit risk scoring project
- Data cleaning
- Data preparation
- Decision trees
- Decision tree learning algorithm
- impurity
- split
- stopping criteria
- Decision trees parameter tuning
- Ensembles and random forest
- Random forest in sklearn
- Random forest parameter tuning
- Gradient boosting
- eXtreme Gradient Boosting - XGBoost
- training
- watchlist
- XGBoost parameter tuning
- learning rate
- max_depth
- min_child_weight
- Testing the final model
- summary
- explore more
- homework

## 7. Midterm Project

## 8. Neural Networks and Deep Learning

- Clothes classification project
- TensorFlow and Keras
- loading the images
- etc
- Using a pre-trained model
- CNNs: convolutional layers
- CNNs: dense layers
- Transfer learning
- Creating the clothes classification model
- Keras functional components
- optimizer
- training the model
- Learning Rate
- Model checkpointing
- Adding more layers
- Dropout
- Data augmentation
- Training a larger clothes classification model
- Using the model with Keras
- summary
- explore more
- homework

## 9. Serverless Deep Learning

- intro
- serverless and AWS Lambda
- tensorflow-lite
- converting the model to TF-lite
- preparing images
- using the model in TF-lite
- putting everything together in a Lambda function
- preparing the docker image
  - testing the image locally
- pusting the image to ECR
- creating the lambda function
- creating the API gateway
- summary
- explore more
- homework

## 10. Kubernetes and TensorFlow-Serving

- intro, serving architecture overview
- saved_model format
- tensorflow-serving
  - running TF-serving locally
- communicating with tf-serving from Jupyter
- creating the gateway service
- introduction to Kubernetes
- creating a cluster on AWS (article)
- preparing the images
  - the TF-serving image
  - the gateway image
- deploying to Kubernetes
  - deployment for tf-serving
  - service for tf-serving
- creating the gateway on Kubernetes
  - deploymnet
  - servince - load balancer
- testing it
- deleting the cluster
- summary
- explore more
- homework

## 11. Kubeflow and KFServing

- intro
- installing Kubeflow on AWS
- preparing the model: uploading to S3
- deploying TF models with KF-serving
- accessing the model
- tranformers
- testing it
- deleting the cluster
- summary
- explore more
- homework - no homework

## 12. Capstone Project

## 13. Article

