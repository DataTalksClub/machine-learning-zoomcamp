## 12. Capstone Project

Now apply everything we learned so far yourself.

That will include:

* Thinking of a problem that's interesting for you and finding a dataset for that
* Describing this problem and explaining how a model could be used
* Preparing the data and doing EDA, analyzing important features
* Training multiple models, tuning their performance and selecting the best model
* Exporting the notebook into a script
* Putting your model into a web service and deploying it locally with docker
* Bonus points for deploying the service to the cloud


### Datasets

* https://www.kaggle.com/datasets and https://www.kaggle.com/competitions
* https://archive.ics.uci.edu/ml/index.php
* https://data.europa.eu/en
* https://www.openml.org/search?type=data
* Add more data here!

### Deliverables

For this project, you repository/folder should contain the following:

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
  * Saving it to a file (e.g. pickle)
* Script `predict.py` (suggested name)
  * Loading the model
  * Serving it via a web serice (e.g. with Flask)
* `Pipenv` and `Pipenv.lock`
  * or equivalents: conda environment file, requirements.txt or pyproject.toml
* `Dockerfile` for running the service
* Deployment
  * URL to the service your deployed or 
  * Video or image of how you interact with the deployed service


### Cheating and plagiarism

Plagiarism in any form is not allowed:

* Taking somebody's else notebooks and projects (in full or partly) and using it for the capstone project
* Re-using your own projects (in full or partly) from other courses and bootcamps
* Re-using your midterm project from ML Zoomcamp

Violating any of this will result in 0 points for this project.


### Submit the results

Submit your results here: https://forms.gle/eLpDSidx8phJxPfH8

### Deadline

The deadline for submitting is 14 December 2021 (Tuesday), 18:00 CET. After that, the form will be closed.


### FAQ

Check the FAQ from the midterm project:

* https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/07-midterm-project#faq



## Peer reviewing

To evaluate the projects, we'll use peer reviewing. This is a great opportunity for your to learn from each other. 

* To get points for your project, your need to evaluate 3 projects of your peers
* You get 3 extra point for each evaluation
* Find the projects to review [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vRsuXlTS_2rR-SxYo_cpnRTZneZ12CPd-L3jva02Lo50JrXjaOzeEF6hdME4y_y3sEjIhKzP43sC1Ci/pubhtml#)


Function for computing the hash of your email:

```python
from hashlib import sha1

def compute_hash(email):
    return sha1(email.lower().encode('utf-8')).hexdigest()
```


Tip: you can use https://nbviewer.org/ to render notebooks if GitHub doesn't work


### Evaluation Criteria

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


### Submitting evaluations

* To submit the evaluations, use this form: https://forms.gle/tHksJjmshDnMM8N57
* You will need to submit this form three times - one for each evaluated project
* Deadline: 20 December (Monday), 17:00 CET. After that, the form will be closed.


## Community notes

* Add your notes here
