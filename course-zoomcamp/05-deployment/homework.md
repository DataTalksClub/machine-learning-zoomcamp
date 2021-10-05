## 5.10 Homework

In this homework, we'll use the churn prediction model trained on a smaller set of features.


## Question 1

* Install Pipenv
* What's the version of pipenv you installed?
* Use `--version` to find out


## Question 2

* Use Pipenv to install Scikit-Learn version 1.0
* What's the first hash for scikit-learn you get in Pipfile.lock? 


## Models

We've prepared a dictionary vectorizer and a model.

They were trained (roughly) using this code:

```
features = ['tenure', 'monthlycharges', 'contract']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

model = LogisticRegression().fit(X, y)
```

And then saved with Pickle. Load them:

* [DictVectorizer](homework/dv.bin)
* [LogisticRegression](homework/model1.bin)


## Question 3

Let's use these models!

* Write a script for loading these models
* Score this customer:

```json
{"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
```

What's the probability that this customer is churning? 


## Question 4

Now let's serve this model as a web service

* Install Flask and Gunicorn (or waitress, if you're on Windows)
* Write Flask code for serving the model
* Now score this customer using `requests`:

```python
url = "YOUR_URL"
customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
requests.post(url, json=customer).json()
```

What's the probability that this customer is churning?


## Docker

For this and the following quesition you'll need Docker. Install it.

For these questions, I prepared a base image. It has these lines:

```docker 
FROM python:3.8.12-slim
WORKDIR /app
COPY ["model2.bin", "dv.bin", "./"]
```

And then I pushed it to [`agrigorev/zoomcamp-model:3.8.12-slim`](https://hub.docker.com/r/agrigorev/zoomcamp-model)

## Question 5

Create your own Dockerfile based on this one

It should start like that:

```docker
FROM agrigorev/zoomcamp-model:3.8.12-slim
# add your stuff here
```

Now complete it:

* Install all the dependencies form the Pipenv file
* Copy your Flask script
* Run it with gunicorn 


When you build your image, what's the digest for `zoomcamp-model:3.8.12-slim`?

Look at the first step of your build log. It should look something like that:

```
Step 1/3 : FROM python:3.8.12-slim
 ---> 2e56f6b0af69
```

## Question 6

Let's run your docker container!

After running it, score the same customer:

```python
url = "YOUR_URL"
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
requests.post(url, json=customer).json()
```

What's the probability that this customer is churning?


## Submit the results

Submit your results here: https://forms.gle/R5v85JBbQ4qgbisv7

It's possible that your answers won't match exactly. If it's the case, select the closest one.


## Deadline

The deadline for submitting is 11 October 2021, 17:00 CET. After that, the form will be closed.



## Publishing to Docker hub

This is just for reference, this is how I published an image to Docker hub:

```bash
docker build -t zoomcamp-test .
docker tag zoomcamp-test:latest  agrigorev/zoomcamp-model:3.8.12-slim
docker push agrigorev/zoomcamp-model:3.8.12-slim
```

## Nagivation

* [Machine Learning Zoomcamp course](../)
* [Session 5: Deploying Machine Learning Models](./)
* Previous: [Explore more](09-explore-more.md)
