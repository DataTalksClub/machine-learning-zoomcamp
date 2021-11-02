# Midterm Project

This is a midterm project to predict survival on [Titanic](https://www.kaggle.com/c/titanic/code).

## Prerequisites

- We use Python 3
- Install [Docker](https://www.docker.com/get-started)
- Install [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- Initialise virtualenv using either `venv` or `.venv` folder name: `virtualenv .venv`
- Activate virtualenv: `source .venv/bin/activate`
- Install all dependencies: `pip3 install -r requirements.txt`

## Train Model

- In order to train a model, run `python3 train.py`

## Run Development Server

- Run Flask server in development mode `python3 predict.py`

If you want to test Flask endpoint, send POST request using cURL to `http://localhost:9696/predict` or use `python3 predict-test.py`

## Build & Run Docker

- In order to build Docker image you can use the following script: `./bin/build.sh`
- If you want to run Docker image locally you can use the following script: `./bin/run.sh`