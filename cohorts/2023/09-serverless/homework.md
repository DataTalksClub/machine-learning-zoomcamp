## Homework

In this homework, we'll deploy the bees vs wasps model we trained in the 
[previous homework](../08-deep-learning/homework.md).

Download the model from here: 

https://github.com/alexeygrigorev/large-datasets/releases/download/wasps-bees/bees-wasps.h5



## Question 1

Now convert this model from Keras to TF-Lite format.

What's the size of the **converted** model?

* 21 Mb
* 43 Mb
* 80 Mb
* 164 Mb


## Question 2

To be able to use this model, we need to know the index of the input and 
the index of the output. 

What's the output index for this model?

* 3
* 7
* 13
* 24


## Preparing the image

You'll need some code for downloading and resizing images. You can use 
this code:

```python
from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img
```

For that, you'll need to have `pillow` installed:

```bash
pip install pillow
```

Let's download and resize this image: 

https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg

Based on the previous homework, what should be the target size for the image?


## Question 3

Now we need to turn the image into numpy array and pre-process it. 

> Tip: Check the previous homework. What was the pre-processing 
> we did there?

After the pre-processing, what's the value in the first pixel, the R channel?

* 0.3450980
* 0.5450980
* 0.7450980
* 0.9450980



## Question 4

Now let's apply this model to this image. What's the output of the model?

* 0.258
* 0.458
* 0.658
* 0.858


## Prepare the lambda code 

Now you need to copy all the code into a separate python file. You will 
need to use this file for the next two questions.

Tip: you can test this file locally with `ipython` or Jupyter Notebook 
by importing the file and invoking the function from this file.  


## Docker 

For the next two questions, we'll use a Docker image that we already 
prepared. This is the Dockerfile that we used for creating the image:

```docker
FROM public.ecr.aws/lambda/python:3.10
COPY bees-wasps-v2.tflite .
```

And pushed it to [`agrigorev/zoomcamp-bees-wasps:v2`](https://hub.docker.com/r/agrigorev/zoomcamp-bees-wasps/tags).

A few notes:

* The image already contains a model and it's not the same model
  as the one we used for questions 1-4.
* The version of Python is 3.10, so you need to use the right wheel for 
  TF-Lite. For Tensorflow 2.14.0, it's https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl


## Question 5

Download the base image `agrigorev/zoomcamp-bees-wasps:v2`. You can easily make it by using [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) command.

So what's the size of this base image?

* 162 Mb
* 362 Mb
* 662 Mb
* 962 Mb

You can get this information when running `docker images` - it'll be in the "SIZE" column.


## Question 6

Now let's extend this docker image, install all the required libraries
and add the code for lambda.

You don't need to include the model in the image. It's already included. 
The name of the file with the model is `bees-wasps-v2.tflite` and it's 
in the current workdir in the image (see the Dockerfile above for the 
reference). 
The provided model requires the same preprocessing for images regarding target size and rescaling the value range than used in homework 8.

Now run the container locally.

Score this image: https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg

What's the output from the model?

* 0.2453
* 0.4453
* 0.6453
* 0.8453


## Publishing it to AWS

Now you can deploy your model to AWS!

* Publish your image to ECR
* Create a lambda function in AWS, use the ECR image
* Give it more RAM and increase the timeout 
* Test it
* Expose the lambda function using API Gateway

This is optional and not graded.


## Publishing to Docker hub

This is just for reference, this is how we published our image to Docker hub:

```bash
docker build -t zoomcamp-bees-wasps -f homework.dockerfile .
docker tag zoomcamp-bees-wasps:latest agrigorev/zoomcamp-bees-wasps:v2
docker push agrigorev/zoomcamp-bees-wasps:v2
```


## Submit the results

- Submit your results here: https://forms.gle/CrgtJVVs64DTGbCp9
- If your answer doesn't match options exactly, select the closest one
- You can submit your solution multiple times. In this case, only the last submission will be used


## Deadline

The deadline for submitting is November 27 (Monday), 23:00 CET. After that the form will be closed.

