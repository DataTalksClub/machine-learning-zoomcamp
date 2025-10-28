## Homework

In this homework, we'll deploy the Straight vs Curly Hair Type model we trained in the 
[previous homework](../08-deep-learning/homework.md).

Download the model from here: 

https://github.com/alexeygrigorev/large-datasets/releases/download/hairstyle/model_2024_hairstyle.keras



## Question 1

Now convert this model from Keras to TF-Lite format.

What's the size of the **converted** model?

* 27 Mb
* 43 Mb
* 77 Mb
* 127 Mb


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

https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg

Based on the previous homework, what should be the target size for the image?


## Question 3

Now we need to turn the image into numpy array and pre-process it. 

> Tip: Check the previous homework. What was the pre-processing 
> we did there?

After the pre-processing, what's the value in the first pixel, the R channel?

* 0.24
* 0.44
* 0.64
* 0.84



## Question 4

Now let's apply this model to this image. What's the output of the model?

* 0.293
* 0.493
* 0.693
* 0.893

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

COPY model_2024_hairstyle_v2.tflite .

RUN pip install numpy==1.23.1
```

Note that it uses Python 3.10. The latest models of TF Lite
do not support Python 3.12 yet, so we need to use 3.10. Also,
for this part, we will use TensorFlow 2.14.0. We have tested
it, and the models created with 2.17 could be served with 2.14.0.

For that image, we also needed to use an older version of numpy
(1.23.1)

The docker image is published to [`agrigorev/model-2024-hairstyle:v3`](https://hub.docker.com/r/agrigorev/model-2024-hairstyle/tags).

A few notes:

* The image already contains a model and it's not the same model
  as the one we used for questions 1-4.
* The wheel for this combination that you'll need to use in your Docker image is https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl


## Question 5

Download the base image `agrigorev/model-2024-hairstyle:v3`. You can do it with [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/).

So what's the size of this base image?

* 182 Mb
* 382 Mb
* 582 Mb
* 782 Mb

You can get this information when running `docker images` - it'll be in the "SIZE" column.


## Question 6

Now let's extend this docker image, install all the required libraries
and add the code for lambda.

You don't need to include the model in the image. It's already included. 
The name of the file with the model is `model_2024_hairstyle_v2.tflite` and it's 
in the current workdir in the image (see the Dockerfile above for the 
reference). 
The provided model requires the same preprocessing for images regarding target size and rescaling the value range than used in homework 8.

Now run the container locally.

Score this image: https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg

What's the output from the model?

* 0.229
* 0.429
* 0.629
* 0.829


## Publishing it to AWS

Now you can deploy your model to AWS!

* Publish your image to ECR
* Create a lambda function in AWS, use the ECR image
* Give it more RAM and increase the timeout 
* Test it
* Expose the lambda function using API Gateway

This is optional and not graded.


## Publishing to Docker hub

Just for the reference, this is how we published our image to Docker hub:

```bash
docker build -t model-2024-hairstyle -f homework.dockerfile .
docker tag model-2024-hairstyle:latest agrigorev/model-2024-hairstyle:v3
docker push agrigorev/model-2024-hairstyle:v3
```

(You don't need to execute this code)

## Submit the results

* Submit your results here: https://courses.datatalks.club/ml-zoomcamp-2024/homework/hw09
* If your answer doesn't match options exactly, select the closest one. If the answer is exactly in between two options, select the higher value.
