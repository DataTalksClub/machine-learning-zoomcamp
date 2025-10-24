# Deploying ML Models with FastAPI and uv

* Video: https://www.youtube.com/watch?v=jzGzw98Eikk

In this workshop we will revise [Module 5](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment) of 
[Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp).

In particular, we will introduce more modern tools:

- Scikit-Learn pipelines
- uv instead of Pipenv
- FastAPI instead of Flask
- Fly.io instead of AWS EBS

In this workshop, we will follow the same order as in the module:

- Saving and loading the model with pickle
- Turning the notebook into a train script
- Introduction to FastAPI (instead of Flask)
- Serving the model with FastAPI
- Input validation with Pydantic (new)
- Virtual environment management - uv (instead of Pipenv)
- Containerization - Docker
- Deployment with Fly.io


## Environment

For the environment, you can use [GitHub Codespaces](https://www.youtube.com/watch?v=pqQFlV3f9Bo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)


Install the required libraries:

```bash
pip install jupyter scikit-learn pandas
```

Then download the starter notebook and save it as workshop-uv-fastapi.ipynb. We will base our work on it.

```bash
wget https://raw.githubusercontent.com/alexeygrigorev/workshops/main/mlzoomcamp-fastapi-uv/starter.ipynb -O workshop-uv-fastapi.ipynb
```

Open it in Jupyter.


## Loading and saving the model

Let's make a prediction for this datapoint:

```python
datapoint = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}
```

We first transform it with the dictionary vectorizer

```python
X = dv.transform(datapoint)
```

And then get the predictions

```python
model.predict_proba(X)[0, 1]
```

Let's save this to pickle:

```python
with open('model.bin', 'wb') as f_out:
    pickle.dump((dv, model), f_out)
```


This is how we load: 

```python
with open('model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)
```

## Scikit-Learn Pipelines

It's not convenient to deal with two objects: `dv` and `model`. 
Let's combine them into one: 


```python
from sklearn.pipeline import make_pipeline

pipeline = make_pipeline(
    DictVectorizer(),
    LogisticRegression(solver='liblinear')
)

pipeline.fit(train_dict, y_train)
```

Now predicting becomes simpler too:

```python
pipeline.predict_proba(datapoint)[0, 1]
```

## Turning the notebook into a script

We can now turn this notebook into a training script:

```bash
jupyter nbconvert --to=script workshop-uv-fastapi.ipynb
mv workshop-uv-fastapi.py train.py
```

Let's edit it.

At the end, we have the code similar to [train.py](train.py)

```python
df = load_data()
pipeline = train_model(df)
save_model(pipeline, 'model.bin')

print('Model saved to model.bin')
```

Let's load the saved model. Create [predict.py](predict.py)
and load the model there:

```python
import pickle

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# apply the model
```

## FastAPI

Now we will turn predict.py into a web service. 

Let's install FastAPI and uvicorn for that:

```bash
pip install fastapi uvicorn
```

The simplest FastAPI app
([created with ChatGPT](https://chatgpt.com/share/6899dc68-03a8-800a-8bd8-9f2218f103e6)
by translating [the old Flask code](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/05-deployment/code/ping.py)).

Let's put it to `ping.py`:


```python
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="ping")

@app.get("/ping")
def ping():
    return "PONG"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
```

Run it:

```bash
python ping.py
```

"Proper" way of running it:

```bash
uvicorn ping:app --host 0.0.0.0 --port 9696 --reload
```

You can now open it in the browser at http://localhost:9696/ping

Or send a request with curl:

```bash
curl localhost:9696/ping
```

No differences with Flask so far. But we can see the docs (not possible with
Flask):

http://localhost:9696/docs


Let's now turn our script into a web application:

```python
import pickle
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="customer-churn-prediction")

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer):
    prob = predict_single(customer)

    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
```

Run it:

```bash
uvicorn predict:app --host 0.0.0.0 --port 9696 --reload
```


Right now it doesn't recognize it as JSON, so let's add type hints:

```python
from typing import Dict, Any

@app.post("/predict")
def predict(customer: Dict[str, Any]):
    prob = predict_single(customer)

    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }
```


Open the docs and send a request:

```json
{
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}
```

We can also do it with curl:

```bash
curl -X 'POST' 'http://localhost:9696/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}'
```

We need to include headers -- FastAPI is more strict about schemas and 
validation than Flask.

To do it from a script, we'll use the requests library. Install it:

```bash
pip install requests
```

Create [`test.py`](test.py):

```python
import requests

url = 'http://localhost:9696/predict'

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

response = requests.post(url, json=customer)
predictions = response.json()

print(predictions)
if predictions['churn']:
    print('customer is likely to churn, send promo')
else:
    print('customer is not likely to churn')
```

## Pydantic and Validation

Another feature of FastAPI that we didn't have in Flask is input and 
output validation

To come up with this schema, I used ChatGPT.
I gave it an example, and also the output of this piece of code:

```python
for n in numerical:
    print(df[n].describe())
    print()

for c in categorical:
    print(df[c].value_counts())
    print()
```

The models (input and output):

```python
from typing import Literal
from pydantic import BaseModel, Field

class Customer(BaseModel):
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=0.0)
    totalcharges: float = Field(..., ge=0.0)


class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool
```

Now we can be more explicit with the input we expect and
the output we generate:

```python
@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    prob = predict_single(customer.model_dump())

    return PredictResponse(
        churn_probability=prob,
        churn=prob >= 0.5
    )
```

Note: if you use `customer.dict()` instead of `model_dump()`, you can get the following warning:

```
PydanticDeprecatedSince20: The `dict` method is deprecated; use `model_dump` instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.11/migration/
```


We now can test how it behaves with incorrect input. Let's add a
field `"whatever": 31337` to our test.py and execute it.

When we run it, nothing happens: it continues working like 
previously.

In order to make Pydantic raise an error, we need to add `model_config`:


```python
from pydantic import ConfigDict


class Customer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ... # rest of the fields
```

Now we will get an error:

```python
response: {'detail': [{'type': 'extra_forbidden', 'loc': ['body', 'whatever'], 'msg': 'Extra inputs are not permitted', 'input': 31337}]}
```

What if we send a value that is not defined by the model? For example,

```json
{
    ...
    "streamingtv": "maybe"
    ...
}
```

In this case, it works as expected: it throws an error:

```python
response: {'detail': [{'type': 'literal_error', 'loc': ['body', 'streamingtv'], 'msg': "Input should be 'no', 'yes' or 'no_internet_service'", 'input': 'maybe', 'ctx': {'expected': "'no', 'yes' or 'no_internet_service'"}}]}
```

## Environment management

It works now but we can have version conflicts with
other projects. So we need to isolate this project from the others.

We will not go into theoretical details about why you want to use
virtual environments. Check [module 5](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/05-deployment/05-pipenv.md) for more information

For that, we will use [`uv`](https://docs.astral.sh/uv/) -- a tool 
for dependency and environment management

Install it:

```bash
pip install uv
```

Initialize the project:

```bash
uv init
``` 

We don't need main.py, so we can remove it:

```bash
rm main.py
```

Notice that it created some files:

- .python-version
- pyproject.toml


We need to have Scikit-Learn and FastAPI for this project.
So let's add them:

```bash
uv add scikit-learn fastapi uvicorn
```

A few more things appeared:

- .venv with all the packages
- uv.lock with a more detailed description of the dependencies

We also have a development dependency -- we won't need it in production:

```bash
uv add --dev requests
```

If we want to run something in this virtual environment, simply 
prefix it with `uv run`:

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload
uv run python test.py
```

When you get a fresh copy of a project that already uses uv, you
can install all the dependencies using the sync command:

```bash
uv sync
```

## Docker

Let's use Docker for complete isolation.
If you want to learn more about Docker, check
[module 5](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/05-deployment/06-docker.md).

In this workshop, we will adjust the [Dockerfile](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/05-deployment/code/Dockerfile)
we created in the module.

First, we need to decide, which Python version we need. You can check 
the version of Python using this command:

```bash
$ python -V
Python 3.13.5
```

So let's use the 3.13.5 image of Python:

```dockerfile
# Use the official Python 3.13.5 slim version based on Debian Bookworm as the base image
FROM python:3.13.5-slim-bookworm

# Copy the 'uv' and 'uvx' executables from the latest uv image into /bin/ in this image
# 'uv' is a fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container to /code
# All subsequent commands will be run from here
WORKDIR /code

# Add the virtual environment's bin directory to the PATH so Python tools work globally
ENV PATH="/code/.venv/bin:$PATH"

# Copy the project configuration files into the container
# pyproject.toml     → project metadata and dependencies
# uv.lock            → locked dependency versions (for reproducibility)
# .python-version    → Python version specification
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Install dependencies exactly as locked in uv.lock, without updating them
RUN uv sync --locked

# Copy application code and model data into the container
COPY "predict.py" "model.bin" ./

# Expose TCP port 9696 so it can be accessed from outside the container
EXPOSE 9696

# Run the application using uvicorn (ASGI server)
# predict:app → refers to 'app' object inside predict.py
# --host 0.0.0.0 → listen on all interfaces
# --port 9696    → listen on port 9696
ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
```

(The comments are added by [ChatGPT](https://chatgpt.com/share/6899ebd9-96f8-800a-819e-093fccadaf7e))

Build it:

```bash
docker build -t predict-churn .
```

And run it:

```bash
docker run -it --rm -p 9696:9696 predict-churn
```

## Deployment

Once the application is dockerized, you can deploy it everywhere. 

In the course, we showed Elastic Beanstalk. Other alternatives:

- Google CloudRun
- AWS App Runner
- Fly.io
- Check the course for contributions from other students, there are a lot of other options

According to ChatGPT, using Fly.io is very simple, so let's do that:

```bash
# for other OS, check https://fly.io/docs/flyctl/install/
# you may also need to replace fly with flyctl
curl -L https://fly.io/install.sh | sh

fly auth signup
fly launch --generate-name
fly deploy
```

Get the URL from the logs, it should be something 
along these lines:

```
Visit your newly deployed app at https://mlzoomcamp-flask-uv.fly.dev/
```

Put the url into test.py and check that it works.

Now you can terminate the deployment

```bash
fly apps destroy <app-name>
```

You can see the list of apps by using the `apps list` command.

Note: check the pricing information.

## Summary

In this workshop we dockerized our ML model and deployed it to the cloud.

If you want to learn more about ML Engineering, check our
[ML Zoomcamp course](https://github.com/DataTalksClub/machine-learning-zoomcamp/).


