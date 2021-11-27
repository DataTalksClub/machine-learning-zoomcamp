# 10. Kubernetes and TensorFlow Serving

We'll deploy the clothes classification model we trained 
previously using Kubernetes and TensorFlow Serving

## 10.1 Overview 

* What we'll cover this week
* Two-tier architecture

## 10.2 TensorFlow Serving

* The saved_model format
* Running TF-Serving locally with Docker
* Invoking the model from Jupyter

## 10.3 Creating a pre-processing service

* Converting the notebook to a Python script
* Wrapping the script into a Flask app

## 10.4 Preparing Docker images

* Preparing the TF-serving image
* Preparing the Gateway servince image

## 10.5 Running everything locally with Docker-compose

* Installing docker-compose 
* Running the service 
* Testing the service

## 10.6 Introduction to Kubernetes

* The anatomy of a Kubernetes cluster
* Setting up a local Kubernetes cluster
* Creating a EKS cluster on AWS

## 10.7 Deploying a simple model to Kubernetes

* Publishing the image to ECR
* Creating a deployment
* Creating a service 

## 10.8 Deploying TF-Serving models to Kubernetes

* Publishing the images
* Creating a deployment and a service for TF-Serving
* Creating a deployment and a service for Gateway
* Testing the service

## 10.9 Summary

* 

## 10.10 Explore more

* 