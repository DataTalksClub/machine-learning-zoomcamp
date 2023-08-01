# 11. Deploying models with KServe (formerly Kubeflow Serving)

This week we'll learn how to use KServe for deploying ML models.

We'll deploy two models: 

* Churn prediction model (Scikit-Learn)
* Clothing classification model (TensorFlow)


## 11.1 Overview 

* Kubeflow and KServe
* What we'll cover this week
* Two-tier architecture


## 11.2 Running KServe locally

* Installing KServe locally with kind
* Deploying an example model from documentation


## 11.3 Deploying a Scikit-Learn model with KServe

* Training the churn model with specific Scikit-Learn version
* Deploying the churn prediction model with KServe


## 11.4 Deploying custom Scikit-Learn images with KServe 

* Customizing the Scikit-Learn image
* Running KServe service locally


## 11.5 Serving TensorFlow models with KServe

* Converting the Keras model to saved_model format
* Deploying the model
* Preparing the input 


## 11.6 KServe transformers

* Why do we need transformers
* Creating a service for pre- and post-processing
* Using existing transformers


## 11.7 Deploying with KServe and EKS 

* Creating an EKS cluster
* Installing KServe on EKS
* Configuring the domain
* Setting up S3 access
* Deploying the clothing model

[Guide used during the video](https://github.com/alexeygrigorev/kubeflow-deep-learning/blob/main/guide.md)


## 11.8 Summary

* Less yaml, faster deployment
* Less stability
* The need for Ops is not gone


## 11.9 Explore more

* Helm charts 
* Kubeflow, Kubeflow pipelines
* Sagemaker
* A lot of vendors that take care of Ops


