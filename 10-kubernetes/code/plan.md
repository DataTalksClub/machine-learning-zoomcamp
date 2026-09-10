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
* Creating the virtual env with Pipenv
* Getting rid of the tensorflow dependency

## 10.4 Running everything locally with Docker-compose

* Preparing the images 
* Installing docker-compose 
* Running the service 
* Testing the service

## 10.5 Introduction to Kubernetes

* The anatomy of a Kubernetes cluster

## 10.6 Deploying a simple service to Kubernetes

* Create a simple ping application in Flask
* Installing kubectl
* Setting up a local Kubernetes cluster with Kind
* Creating a deployment
* Creating a service 

## 10.7 Deploying TensorFlow models to Kubernetes

* Deploying the TF-Serving model
* Deploying the Gateway
* Testing the service

## 10.8 Deploying to EKS

* Creating a EKS cluster on AWS
* Publishing the image to ECR

## 10.9 Summary

* TF-Serving is a system for deploying TensorFlow models
* When using TF-Serving, we need a component for pre-processing 
* Kubernetes is a container orchestration platform
* To deploy something on Kubernetes, we need to specify a deployment and a service
* You can use Docker compose and Kind for local experiments 

## 10.10 Explore more

* Other local Kuberneteses: minikube, k3d, k3s, microk8s, EKS Anywhere
* [Rancher desktop](https://rancherdesktop.io/)
* Docker desktop
* [Lens](https://k8slens.dev/)
* Many cloud providers have Kubernetes: GCP, Azure, Digital ocean and others. Look for "Managed Kubernetes" in your favourite search engine
* Deploy the model from previous modules and from your project with Kubernetes
* Learn about Kubernetes namespaces. Here we used the default namespace
