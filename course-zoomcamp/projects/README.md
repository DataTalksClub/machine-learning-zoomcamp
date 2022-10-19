## Projects 

The idea is that you now apply everything we learned so far yourself.

There are three projects in this course:

* Midterm project
* Capstone 1
* Capstone 2


This is what you need to do for each project

* Think of a problem that's interesting for you and find a dataset for that
* Describe this problem and explain how a model could be used
* Prepare the data and doing EDA, analyze important features
* Train multiple models, tune their performance and select the best model
* Export the notebook into a script
* Put your model into a web service and deploy it locally with Docker
* Bonus points for deploying the service to the cloud


## Midterm project

TBA

## Capstone 1

TBA

## Capstone 2

TBA


## Deliverables

For a project, you repository/folder should contain the following:

* `README.md` with
  * Description of the problem
  * Instructions on how to run the project
* Data
  * You should either commit the dataset you used or have clear instructions how to download the dataset
* Notebook (suggested name - `notebook.ipynb`) with
  * Data preparation and data clearning
  * EDA, feature importance analysis
  * Model selection process and parameter tuning
* Script `train.py` (suggested name)
  * Training the final model
  * Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
* Script `predict.py` (suggested name)
  * Loading the model
  * Serving it via a web serice (with Flask or specialized sofware - BentoML, KServe, etc)
* Files with dependencies
  * `Pipenv` and `Pipenv.lock` if you use Pipenv
  * `bentofile.yaml` if you use BentoML
  * or equivalents: conda environment file, requirements.txt or pyproject.toml
* `Dockerfile` for running the service
* Deployment
  * URL to the service your deployed or
  * Video or image of how you interact with the deployed service


## Peer reviewing

To evaluate the projects, we'll use peer reviewing. This is a great opportunity for your to learn from each other.

* To get points for your project, your need to evaluate 3 projects of your peers
* You get 3 extra point for each evaluation

Tip: you can use https://nbviewer.org/ to render notebooks if GitHub doesn't work


## Evaluation Criteria

The project will be evaluated using these criteria:

* Problem description
* EDA
* Model training
* Exporting notebook to script
* Model deployment
* Reproducibility
* Dependency and environment management
* Containerization
* Cloud deployment

[Criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCwqAtkjl07MTW-SxWUK9GUvMQ3Pv_fF8UadcuIYLgHa0PlNu9BRWtfLgivI8xSCncQs82HDwGXSm3/pubhtml)


## Cheating and plagiarism

Plagiarism in any form is not allowed. Examples of plagiarism

* Taking somebody's else notebooks and projects (in full or partly) and using it for the capstone project
* Re-using your own projects (in full or partly) from other courses and bootcamps
* Re-using your midterm project from ML Zoomcamp in capstone
* Re-using your ML Zoomcamp from previous iterations of the course

Violating any of this will result in 0 points for this project.


## Datasets

* [A list with datasets from our Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_7_project/datasets.md)
* https://www.kaggle.com/datasets and https://www.kaggle.com/competitions
* https://archive.ics.uci.edu/ml/index.php
* https://data.europa.eu/en
* https://www.openml.org/search?type=data
* https://www.tensorflow.org/datasets/catalog/overview
* [Soocer data](https://github.com/statsbomb/open-data)
* https://newzealand.ai/public-data-sets
* Add more data here!


## FAQ

**Q**: Do I have to run the code and make sure it works?

> It's recommended that you do that, but you don't _have_ to do it.

**Q**: What if I see an error? What if I run something and it doesn't work?

> But if you spot an error somewhere and you see that the code clearly doesn't work, then you
> give 0 points to the respective criterium. E.g. if you see an error in Dockerfile,
> then you give 0 points to the "containerization" dimension.



## Zoomcamp 2021

You can check the projects from ML Zoomcamp 2021 here:

* [Midterm projects](../cohorts/2021/07-midterm-project/)
* [Capstone 1](../cohorts/2021/12-capstone/)
* [Capstone 2](../cohorts/2021/14-project/)

