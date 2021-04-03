# Chapter 5. Deployment

## Preparation

If you don't have the model from the previous chapter, run `05-deploy.ipynb` to generate the pickle file.

## Running without Docker

First, install flask:

```bash
pip install flask
```

Run the service:

```bash
python churn_serving.py
```

Test it from python:

```python
import requests
url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer)
result = response.json()
```

## Managing dependencies with Pipenv

Install `pipenv`:

```bash
pip install pipenv
```

Install the depencencies from the [Pipfile](Pipfile):

```bash
pipenv install
```

Enter the pipenv virtual environment:

```bash
pipenv shell
```

And run the code:

```bash
python churn_serving.py
```

Alternatively, you can do both steps with one command:

```bash
pipenv run python churn_serving.py
```

Now you can use the same code for testing the model locally.


## Running with Docker

Build the image (defined in [Dockerfile](Dockerfile))

```bash
docker build -t churn-prediction .
```

Run it:

```bash
docker run -it -p 9696:9696 churn-prediction:latest
```