# 5. Deploying Machine Learning models 

We'll use the same model we trained and evaluated
previously - the churn prediction model. Now we'll
deploy it as a web service.

## 5.1 Intro / Session overview

* What we will cover this week

## 5.2 Saving and loading the model

* Saving the model to pickle
* Loading the model from pickle
* Turning our notebook into a Python script

## 5.3 Web services: introduction to Flask

* Writing a simple ping/pong app
* Querying it with `curl` and browser

## 5.4 Serving the churn model with Flask

* Wrapping the predict script into a Flask app
* Querying it with `requests` 
* Preparing for production: gunicorn
* Running it on Windows with waitress

## 5.5 Python virtual environment: Pipenv

* Dependency and environment management
* Why we need virtual environment
* Installing Pipenv
* Installing libraries with Pipenv
* Running things with Pipenv

## 5.6 Environment management: Docker

* Why we need Docker
* Running a Python image with docker
* Dockerfile
* Building a docker image
* Running a docker image

## 5.7 Deployment to the cloud: AWS Elastic Beanstalk (optional)

* Installing the eb cli
* Running eb locally
* Deploying the model

## 5.8 Summary

* Save models with picke
* Use Flask to turn the model into a web service
* Use a dependency & env manager
* Package it in Docker
* Deploy to the cloud


## 5.9 Explore more

* Flask is not the only framework for creating web services. Try others, e.g. FastAPI
* Experiment with other ways of managing environment, e.g. virtual env, conda, poetry.
* Explore other ways of deploying web services, e.g. GCP, Azure, Heroku, Python Anywhere, etc

