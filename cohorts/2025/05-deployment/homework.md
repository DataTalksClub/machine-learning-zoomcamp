## Homework

> Note: sometimes your answer doesn't match one of the options exactly. 
> That's fine. 
> Select the option that's closest to your solution.
> If it's exactly in between two options, select the higher value.

We recommend using python 3.12 or 3.13 in this homework.

In this homework, we're going to continue working with the lead scoring dataset. You don't need the dataset: we will provide the model for you.


## Question 1

* Install `uv`
* What's the version of uv you installed?
* Use `--version` to find out


## Initialize an empty uv project

You should create an empty folder for homework
and do it there. 


## Question 2

* Use uv to install Scikit-Learn version 1.6.1 
* What's the first hash for Scikit-Learn you get in the lock file?
* Include the entire string starting with sha256:, don't include quotes


## Models

We have prepared a pipeline with a dictionary vectorizer and a model.

It was trained (roughly) using this code:

```python
categorical = ['lead_source']
numeric = ['number_of_courses_viewed', 'annual_income']

df[categorical] = df[categorical].fillna('NA')
df[numeric] = df[numeric].fillna(0)

train_dict = df[categorical + numeric].to_dict(orient='records')

pipeline = make_pipeline(
    DictVectorizer(),
    LogisticRegression(solver='liblinear')
)

pipeline.fit(train_dict, y_train)
```

> **Note**: You don't need to train the model. This code is just for your reference.

And then saved with Pickle. Download it [here](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/cohorts/2025/05-deployment/pipeline_v1.bin).

With `wget`:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/raw/refs/heads/master/cohorts/2025/05-deployment/pipeline_v1.bin
```


## Question 3

Let's use the model!

* Write a script for loading the pipeline with pickle
* Score this record:

```json
{
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}
```

What's the probability that this lead will convert? 

* 0.333
* 0.533
* 0.733
* 0.933

If you're getting errors when unpickling the files, check their checksum:

```bash
$ md5sum pipeline_v1.bin
7d17d2e4dfbaf1e408e1a62e6e880d49 *pipeline_v1.bin
```


## Question 4

Now let's serve this model as a web service

* Install FastAPI
* Write FastAPI code for serving the model
* Now score this client using `requests`:

```python
url = "YOUR_URL"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
requests.post(url, json=client).json()
```

What's the probability that this client will get a subscription?

* 0.334
* 0.534
* 0.734
* 0.934


## Docker

Install [Docker](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/05-deployment/06-docker.md). 
We will use it for the next two questions.

For these questions, we prepared a base image: `agrigorev/zoomcamp-model:2025`. 
You'll need to use it (see Question 5 for an example).

This image is based on `3.13.5-slim-bookworm` and has
a pipeline with logistic regression (a different one)
as well a dictionary vectorizer inside. 

This is how the Dockerfile for this image looks like:

```docker 
FROM python:3.13.5-slim-bookworm
WORKDIR /code
COPY pipeline_v2.bin .
```

We already built it and then pushed it to [`agrigorev/zoomcamp-model:2025`](https://hub.docker.com/r/agrigorev/zoomcamp-model).

> **Note**: You don't need to build this docker image, it's just for your reference.


## Question 5

Download the base image `agrigorev/zoomcamp-model:2025`. You can easily make it by using [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) command.

So what's the size of this base image?

* 45 MB
* 121 MB
* 245 MB
* 330 MB

You can get this information when running `docker images` - it'll be in the "SIZE" column.


## Dockerfile

Now create your own `Dockerfile` based on the image we prepared.

It should start like that:

```docker
FROM agrigorev/zoomcamp-model:2025
# add your stuff here
```

Now complete it:

* Install all the dependencies from pyproject.toml
* Copy your FastAPI script
* Run it with uvicorn 

After that, you can build your docker image.


## Question 6

Let's run your docker container!

After running it, score this client once again:

```python
url = "YOUR_URL"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
requests.post(url, json=client).json()
```

What's the probability that this lead will convert?

* 0.39
* 0.59
* 0.79
* 0.99


## Submit the results

* Submit your results here: https://courses.datatalks.club/ml-zoomcamp-2025/homework/hw05
* If your answer doesn't match options exactly, select the closest one. If the answer is exactly in between two options, select the higher value.



## Publishing to Docker hub

This is just for reference, this is how we published an image to Docker hub.

`Dockerfile_base`: 

```dockerfile
FROM python:3.13.5-slim-bookworm
WORKDIR /code
COPY pipeline_v2.bin .
```

Publishing:

```bash
docker build -t mlzoomcamp2025_hw5 -f Dockerfile_base .
docker tag mlzoomcamp2025_hw5:latest agrigorev/zoomcamp-model:2025
docker push agrigorev/zoomcamp-model:2025
```
