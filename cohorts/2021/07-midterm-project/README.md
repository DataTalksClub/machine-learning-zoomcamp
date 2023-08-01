## 7. Midterm Project

The idea is that you now apply everything we learned so far yourself.

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


### Submit the results

Submit your results here: https://forms.gle/5JLFUwwXaUDssVKt7

### Deadline

The deadline for submitting is 3 November 2021 (Wednesday), 12:00 (noon) CET. After that, the form will be closed.


### FAQ

**Q**: Can I use poetry / virtual env for managing dependencies; catboost for boosting and FastAPI for creating a web service?

> Yes, you can use any library you want. But please make sure to document everything and clearly explain what you use.
> Think of your peers who will review it - they don't necessarily know what these libraries are. 
> Please give them enough context to understand your project.

**Q**: Can multiple people use the same dataset?

> Yes, there's no way to control it or enforce. So it's totally okay if you and somebody else use the same dataset. 




## Peer reviewing

To evaluate the projects, we'll use peer reviewing. This is a great opportunity for your to learn from each other. 

* To get points for your project, your need to evaluate 3 projects of your peers
* You get 3 extra point for each evaluation

To find the projects you need to review, use [this table](https://docs.google.com/spreadsheets/d/e/2PACX-1vRo05lqGFkl7Jtt4o9Dqqk8JEA-U956-sxJVT-klWrKp8nTvboOkyyYVH-Z4sccFdpvfZhd40eGhU2J/pubhtml)

* Hash your email
* Find your email in the `reviewer_hash` column
* You'll have three other projects there - that's what you'll need to evaluate

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
* Dependency and environment management
* Containerization
* Cloud deployment

[Detailed criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQo-cOOGMA-ddbp6FgxusNBjS_HOmWaOYtvO7z-wk_TcCnPOBAza9s8Uj_eqfKGadoU0741cCGd95qI/pubhtml)


### Submitting evaluations

* To submit the evaluations, use this form: https://forms.gle/AMFvMNnfwEeTQxaj8
* You will need to submit this form three times - one for each evaluated project
* Deadline: 10 November (Wednesday), 12:00 (noon) CET.  After that, the form will be closed.


### FAQ 

**Q**: Do I have to run the code and make sure it works?

> It's recommended that you do that, but you don't _have_ to do it. 

**Q**: What if I see an error? What if I run something and it doesn't work?

> But if you spot an error somewhere and you see that the code clearly doesn't work, then you 
> give 0 points to the respective criterium. E.g. if you see an error in Dockerfile, 
> then you give 0 points to the "containerization" dimension. 

**Q**: Somebody submitted a project they did as a part of some other course. What to do?

> That's not good, but we didn't explicitly say it's not allowed. We'll change that for the next project,
> but for the midterm project, you can evaluate it as if it was specifically made for this course.


**Q**: Somebody just copied a Kaggle Kernel (or some other publicly available project) and 
submitted this as their project.

> That's definitely not good. For the next project, we'll have an explicit policy that forbids
> doing it. For this project, you should evaluate the copied parts as 0. For example,
> if the model trianing part was copied, but the deployment wasn't, the model training part gets 0 
> points, but the model deployment part gets the points.


## Office Hours 2021

We discussed the project in detail in three office hours sessions

### Office Hours Week #7 

* [Video](https://www.youtube.com/watch?v=wWBm6MHu5u8)

### Office Hours Week #8

* [Video](https://www.youtube.com/watch?v=3bo7I9LaN7o)
* [Notebook](week8-office-hours.ipynb)

### Office Hours Week #9

* [Video](https://www.youtube.com/watch?v=yZ15WyKb5o4)
* [Notebook](week9-office-hours.ipynb)

### Office Hours Week #10

* [Video](https://www.youtube.com/watch?v=jT0JTlPsAQ0)
* [Notebook](week10-office-hours.ipynb)


## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Alvaro Navas' Notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/07_misc.md)
* Add your notes here