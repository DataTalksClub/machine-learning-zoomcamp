## 9.10 Homework

In this homework, we'll deploy the dogs vs cats model we trained in the previous 
homework.

Download the model from here: 

https://github.com/alexeygrigorev/large-datasets/releases/download/dogs-cats-model/dogs_cats_10_0.687.h5


## Question 1

Now convert this model from Keras to TF-Lite format.

What's the size of the converted model? 


## Question 2

To be able to use this model, we need to know the index of the input and 
the index of the output. 

What's the output index for this model? 


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

For that, you'll need to have pillow installed:

```bash
pip install pillow
```

Let's download and resize this image: 

https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg

Based on [the solution of the previous homework](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/08-deep-learning/CNN_solution.ipynb),
what should be the target size for the image?


## Question 3

Now we need to turn the image into an numpy array and pre-process it. 

After the pre-processing, what's the value in the first pixel, the R channel?


## Question 4 

Now let's apply this model to this image. What's the output of the model?


## 

## Question 5





## Notes

Add notes from the video (PRs are welcome)


<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>


## Nagivation

* [Machine Learning Zoomcamp course](../)
* [Session 9: Serverless Deep Learning](./)
* Previous: [Explore more](09-explore-more.md)