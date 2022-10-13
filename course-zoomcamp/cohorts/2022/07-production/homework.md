## Homework

In this homework, we will use Credit Risk Data from module 6

> Note: sometimes your answer doesn't match one of the options exactly. That's fine. 
Select the option that's closest to your solution.

The goal of this homework is to familiarize you with BentoML and 

## Question 1

* Install BentoML
* What's the version of BentoML you installed?
* Use `--version` to find out


## Question 2

* Run the notebook from module 6 and save the credit risk model with BentoML
* How big approximately is the saved BentoML model?

* 524kb
* 224kb
* 114kb
* 68kb

## Question 3

Say you have the following data that you're sending to your service:

```json
{
  "name": "Tim",
  "age": 37,
  "country": "US",
  "rating": 3.14
}
```

What would the pydantic class look like? You can name the class "Person"

## Question 4

We've prepared a model for you that you can import using:
```bash
bentoml models import s3://
```

What version of sklearn was this model trained with?

## Question 5 

Create a bento out of this sklearn model

install this requirements file

The annotation for the bento endpoint should be:
@svc.api(...)

Send this array to the bento:
[0.25,0.35,0.45]

What's the probability that's returned? 

* 0.162
* 0.391
* 0.601
* 0.993

You can use curl or the swagger UI. What value does it return?

## Question 6

Add Validation to this bento by enforcing shape (-1,3)
Send this array to the bento:
[0.25,0.35]

What is the resulting error?

* Can't use your data unfortunately...
* Can't use your data unfortunately...
* Can't use your data unfortunately...
* Can't use your data unfortunately...


## Question 7

install locust
use the following locust file

Configure 100 users and send

Now download this model

Test out the first model and the second model, which one performance better at higher volumes?


## Question 8

Go to this Bento deployment of Stable Diffusion: http://54.176.205.174/

Use the txt2image endpoint and update the prompt to: "A cartoon dragon with sunglasses"
- Don't change the seed, it should be 0 by default

What is the resulting image?

1. <>
2. <>
3. <>
4. <>


## Submit the results

* Submit your results here: https://forms.gle/jU2we8f9WeLgX3qa6
* You can submit your solution multiple times. In this case, only the last submission will be used 
* If your answer doesn't match options exactly, select the closest one


## Deadline

The deadline for submitting is **10 October 2022 (Monday), 23:00 CEST (Berlin time)**. 

After that, the form will be closed.
