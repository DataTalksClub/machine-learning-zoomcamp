## 8.2 TensorFlow and Keras

<a href="https://www.youtube.com/watch?v=R6o_CUmoN9Q&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-02.jpg"></a>
 
[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-8-neural-networks-and-deep-learning-250592316)


- TensorFlow is a library to train deep learning models and Keras is higher level abstraction on the top of TensorFlow. Keras used to be separate library but from tensorflow 2+ version, keras became part of the tensorflow library. The libraries can be installed using `pip install tensorflow` (for CPU and GPU). However, additional setup is required to integrate TensorFlow with GPU. 
- Neural networks expect an image of a certain size, therefore, we need to provide the image size in `target_size` parameter of the `load_img` function.
- Each image consists of pixel and each of these pixels has the shape of 3 dimensions ***(height, width, color channels)***
- A typical color image consists of three color channels: `red`, `green` and `blue`. Each color channel has 8 bits or 1 byte and can represent distinct values between 0-256 (uint8 type).

**Classes, functions, and methods**:

- `import tensorflow as tf`: to import tensorflow library
- `import tensorflow as keras`: to import keras
- `from tensorflow.keras.preprocessing.image import load_img`: to import load_img function
- `load_img('path/to/image', targe_size=(150,150))`: to load the image of 150 x 150 size in PIL format
- `np.array(img)`: convert image into a numpy array of 3D shape, where each row of the array represents the value of red, green, and blue color channels of one pixel in the image.


## Notes

Add notes from the video (PRs are welcome)

* tensorflow and keras as deep learning libraries
* end-to-end open source machine learning framework
* tensorflow as library for training deep learning models
* keras as high-level abstraction on top of tensorflow
* installing tensorflow
* local vs cloud configuration
* loading and preprocessing images
* keras is part of tensorflow since version 2.0
* working with different image sizes
* processing images using the python pillow library
* encoding images as numpy arrays
* image size (i.e. 150 x 150 pixels) multiplied by number of colors (i.e. RGB) equals shape of array
* numpy array dtype as unsigned int8 (uint8) which includes the range from 0 to 255

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 8: Neural Networks and Deep Learning](./)
* Previous: [Setting up the Environment on Saturn Cloud](01b-saturn-cloud.md)
* Next: [Pre-trained convolutional neural networks](03-pretrained-models.md)
