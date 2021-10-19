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


## Submit the results

Submit your results here: https://forms.gle/5JLFUwwXaUDssVKt7


## Deadline

The deadline for submitting is 1 November 2021, 17:00 CET (Monday). After that, the form will be closed.

## FAQ

**Q**: Can I use poetry / virtual env for managing dependencies; catboost for boosting and FastAPI for creating a web service?

> Yes, you can use any library you want. But please make sure to document everything and clearly explain what you use.
> Think of your peers who will review it - they don't necessarily know what these libraries are. 
> Please give them enough context to understand your project.

**Q**: Can multiple people use the same dataset?

> Yes, there's no way to control it or enforce. So it's totally okay if you and somebody else use the same dataset. 
