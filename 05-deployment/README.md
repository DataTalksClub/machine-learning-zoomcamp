## 5. Deploying Machine Learning Models

Note: these materials are partly outdated, which
is why we recorded a workshop that updates this module.
You will find the materials in the [workshop/](workshop/) folder

The theory in the module is still relevant, which is why we suggest you
to watch both the workshop and the module content. While watching 
the module content, focus on the theory part. The practical 
part is all covered in the workshop. 


- 5.1 [Intro / Session overview](01-intro.md) - Outline the module plan for turning the churn model into a web service with pickle, Flask, Pipenv, and Docker.
- 5.2 [Saving and loading the model](02-pickle.md) - Save the trained DictVectorizer and model with pickle, load them back, and move the training code into a script.
- 5.3 [Web services: introduction to Flask](03-flask-intro.md) - Build a minimal Flask ping service with a GET route that returns PONG, then test it with curl.
- 5.4 [Serving the churn model with Flask](04-flask-deployment.md) - Serve churn predictions from a Flask POST endpoint, test it with requests, and run it under gunicorn or waitress.
- 5.5 [Python virtual environment: Pipenv](05-pipenv.md) - Pin project dependencies in a Pipenv virtual environment with Pipfile and Pipfile.lock, then run the service inside it.
- 5.6 [Environment management: Docker](06-docker.md) - Package the churn service into a Docker image with a Dockerfile, then build and run it with port 9696 published.
- 5.7 [Deployment to the cloud: AWS Elastic Beanstalk (optional)](07-aws-eb.md) - Deploy the churn Docker image to AWS Elastic Beanstalk with the EB CLI, then test and terminate the environment.
- 5.8 [Summary](08-summary.md) - Recap the deployment module, from pickle and Flask to Pipenv, Docker, and AWS Elastic Beanstalk.
- 5.9 [Explore more](09-explore-more.md) - Suggest alternatives to explore, including FastAPI, conda or poetry, and other cloud or hosting platforms.


How to watch it:

- First, watch the units 5.1-5.6 
- Then watch the workshop and do the practice 
- Finally, do the homework


## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Notes from Alvaro Navas](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/05a_deployment.md)
* [Docker notes](https://github.com/ayoub-berdeddouch/mlbookcamp-homeworks/blob/main/Deployment/README.md)
* [Notes from froukje](https://github.com/froukje/ml-zoomcamp/blob/main/week5/lecture/Lecture_5_deploying_ml_models.ipynb)
* [WSL + Docker notes](https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/Week_5-flask_and_docker_for_deployment/readme.md)
* [Notes from Hareesh Tummala](https://github.com/tummala-hareesh/ml_zoomcamp_ht/blob/main/notes/week-5-notes.md)
* [Notes about Docker](https://github.com/shayansm2/eng-notebook/tree/main/docker)
* [Notes about Deployment, Pipenv, Flask, Docker by Oscar Garcia](https://github.com/ozkary/machine-learning-engineering/tree/main/05-deployment)
* [Notebook with commands for pipenv, flask, gunicorn, and Docker](https://github.com/javier-cp6/ml-zoomcamp/blob/main/05-deployment/05-train-churn-model.ipynb)
* [Notes from Peter Ernicke](https://knowmledge.com/category/courses/ml-zoomcamp/model-deployment/)
* [Notes from Kemal Dahha](https://github.com/kemaldahha/machine-learning-course/blob/main/week_5_notes.ipynb)
* [Notes from Williams Alnice](https://github.com/nice-bills/ml_zoomcamp/tree/main/module_5)
* [Cohort 2025| Notes by Nitin Gupta](https://github.com/niting9881/ML-zoomcamp-local/blob/main/05-deployment/README.md)
* Add your notes here

### Deployment tutorials

* [Using PythonAnywhere to host your Python Web App for free!!! (an an alternative to AWS/Azure/Google cloud)](https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-pythonanywhere.md)
* [Deploy Churn Service on Heroku](https://github.com/razekmaiden/churn_service_heroku.git)
* [Installing and using pipenv and Docker on Intel Macs](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/05b_virtenvs.md)
* [Azure Guide](https://github.com/yusyel/guides/tree/master/azure#1-creating-azure-account)
* Add your tutorials here

