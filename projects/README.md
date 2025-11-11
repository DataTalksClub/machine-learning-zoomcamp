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

## Videos

[Submit and evaluate Zoomcamp projects 🎥](https://www.loom.com/share/4f5c155c550e48ddb54b71ba76516b04)

We did a few office hours sessions where we explained how you go about the projects. 

Check them out:

* [ML Zoomcamp 2023 Office Hours (pre-midterm)](https://www.youtube.com/live/GuJkBzyGxyc)
* [ML Zoomcamp 2022 - Office Hours (midterm project)](https://www.youtube.com/live/AcB-Iz8h5tc)
* [2021 Office hours #7](https://www.youtube.com/live/wWBm6MHu5u8) and [2021 Office hours #8](https://www.youtube.com/live/3bo7I9LaN7o) (check #8 if you want to use text)

## Deliverables

For a project, you repository/folder should contain the following:

* `README.md` with
  * Description of the problem
  * Instructions on how to run the project
* Data
  * You should either commit the dataset you used or have clear instructions how to download the dataset
* Notebook (suggested name - `notebook.ipynb`) with
  * Data preparation and data cleaning
  * EDA, feature importance analysis
  * Model selection process and parameter tuning
* Script `train.py` (suggested name)
  * Training the final model
  * Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
* Script `predict.py` (suggested name)
  * Loading the model
  * Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)
* Files with dependencies
  * `Pipenv` and `Pipenv.lock` if you use Pipenv
  * or equivalents: conda environment file, requirements.txt or pyproject.toml
* `Dockerfile` for running the service
* Deployment
  * URL to the service you deployed or
  * Video or image of how you interact with the deployed service


## Peer reviewing

> [!IMPORTANT]  
> To evaluate the projects, we'll use peer reviewing. This is a great opportunity for you to learn from each other.
> * To get points for your project, you need to evaluate 3 projects of your peers
> * You get 3 extra points for each evaluation
> * If you don't evaluate your peers, you fail the project

Tip: you can use https://nbviewer.org/ to render notebooks if GitHub doesn't work


## Evaluation Criteria

The project will be evaluated using these criteria:
* Problem description
    * 0 points: Problem is not described
    * 1 point: Problem is described in README birefly without much details
    * 2 points: Problem is described in README with enough context, so it's clear what the problem is and how the solution
will be used
* EDA
    * 0 points: No EDA
    * 1 point: Basic EDA (looking at min-max values, checking for missing values)
    * 2 points: Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis)
      For images: analyzing the content of the images.
      For texts: frequent words, word clouds, etc
* Model training
    * 0 points: No model training
    * 1 point: Trained only one model, no parameter tuning
    * 2 points: Trained multiple models (linear and tree-based).
      For neural networks: tried multiple variations - with dropout or without, with extra inner layers or without 
    * 3 points: Trained multiple models and tuned their parameters.
      For neural networks: same as previous, but also with tuning: adjusting learning rate, dropout rate, size of the inner layer, etc.
* Exporting notebook to script
    * 0 points: No script for training a model
    * 1 point: The logic for training the model is exported to a separate script
* Reproducibility
    * 0 points: Not possitble to execute the notebook and the training script. Data is missing or it's not easiliy accessible
    * 1 point: It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data
* Model deployment
    * 0 points: Model is not deployed
    * 1 point: Model is deployed (with Flask, BentoML or a similar framework)
* Dependency and enviroment management
    * 0 points: No dependency management
    * 1 point: Provided a file with dependencies (requirements.txt, pipfile, bentofile.yaml with dependencies, etc)
    * 2 points: Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to
activate the env
* Containerization
    * 0 points: No containerization
    * 1 point: Dockerfile is provided or a tool that creates a docker image is used (e.g. BentoML)
    * 2 points: The application is containerized and the README describes how to build a container and how to run it
* Cloud deployment
    * 0 points: No deployment to the cloud
    * 1 point: Docs describe clearly (with code) how to deploy the service to cloud or kubernetes cluster (local or remote)
    * 2 points: There's code for deployment to cloud or kubernetes cluster (local or remote). There's a URL for testing - or video/screenshot of testing it

Total max 16 points

Or the same in table format [Criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCwqAtkjl07MTW-SxWUK9GUvMQ3Pv_fF8UadcuIYLgHa0PlNu9BRWtfLgivI8xSCncQs82HDwGXSm3/pubhtml)


## Cheating and plagiarism

Plagiarism in any form is not allowed. Examples of plagiarism:

* Taking somebody's else notebooks and projects (in full or partly) and using it for the capstone project
* Re-using your own projects (in full or partly) from other courses and bootcamps
* Re-using your midterm project from ML Zoomcamp in capstone
* Re-using your ML Zoomcamp from previous iterations of the course

Violating any of this will result in 0 points for this project.

## FAQ


**Q**: Can I use poetry / virtual env for managing dependencies; catboost for boosting and FastAPI for creating a web service?

> Yes, you can use any library you want. But please make sure to document everything and clearly explain what you use.
> Think of your peers who will review it - they don't necessarily know what these libraries are. 
> Please give them enough context to understand your project.

**Q**: Can multiple people use the same dataset?

> Yes, there's no way to control it or enforce. So it's totally okay if you and somebody else use the same dataset. 

**Q**: For peer reviewing, do I have to run the code and make sure it works?

> It's recommended that you do that, but you don't _have_ to do it.

**Q**: What if I see an error? What if I run something and it doesn't work?

> If you spot an error somewhere and you see that the code clearly doesn't work, then you
> give 0 points to the respective criterium. E.g. if you see an error in Dockerfile,
> then you give 0 points to the "containerization" dimension.

**Q**: Should I include a project title, and what happens if I leave the README file empty?

> It's highly recommended to create a new repository for your project (not inside an existing repo) with a meaningful title, such as
> "Car Price Prediction" or "Heart Risk Prediction" and including as many details as possible in the README file. ChatGPT can assist you with this. Doing so will not only make it easier to showcase your project for potential job opportunities but also have it featured on the [Projects Gallery App](#projects-gallery).
> If you leave the README file empty or with minimal details, there may be point deductions as per the [Evaluation Criteria](#evaluation-criteria).

## Resources

### Datasets

* [A list with datasets from our Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/projects/datasets.md)
* [kaggle Datasets](https://www.kaggle.com/datasets) and [kaggle Competitions](https://www.kaggle.com/competitions)
* [Tensorflow Datasets](https://www.tensorflow.org/datasets/catalog/overview)
* [PyTorch - Image Datasets, Text Datasets, and Audio Datasets](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) links in first paragraph
* [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
* [OpenML Datasets](https://www.openml.org/search?type=data)
* [OECD database](https://stats.oecd.org/index.aspx?lang=en)
* [European data](https://data.europa.eu/en)
* [Urban Data Platform Hamburg](https://www.en.urbandataplatform.hamburg/find-data)
* [New Zealand Data Sets](https://newzealand.ai/public-data-sets)
* [Open Images Dataset V7 and Extensions](https://storage.googleapis.com/openimages/web/index.html)
* [deeplake - Machine Learning Datasets](https://datasets.activeloop.ai/docs/ml/datasets/)
* [Soccer data](https://github.com/statsbomb/open-data)
* Add more data here!

### Projects Gallery

Explore a collection of projects completed by members of our community. The projects cover a wide range of topics and utilize different tools and techniques. Feel free to delve into any project and see how others have tackled real-world problems with data, structured their code, and presented their findings. It's a great resource to learn and get ideas for your own projects.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://datatalksclub-projects.streamlit.app/)

### Zoomcamp 2024

* [Midterm project](../cohorts/2024/projects.md#midterm-project)
* [Capstone 1](../cohorts/2024/projects.md#capstone-1)
* [Capstone 2](../cohorts/2024/projects.md#capstone-2)

### Zoomcamp 2023

* [Midterm project](../cohorts/2023/projects.md#midterm-project)
* [Capstone 1](../cohorts/2023/projects.md#capstone-1)
* [Capstone 2](../cohorts/2023/projects.md#capstone-2)


### Zoomcamp 2022

* [Midterm project](../cohorts/2022/projects.md#midterm-project)
* [Capstone 1](../cohorts/2022/projects.md#capstone-1)
* [Capstone 2](../cohorts/2022/projects.md#capstone-2)


### Zoomcamp 2021

* [Midterm project](../cohorts/2021/07-midterm-project/)
* [Capstone 1](../cohorts/2021/12-capstone/)
* [Capstone 2](../cohorts/2021/14-project/)

