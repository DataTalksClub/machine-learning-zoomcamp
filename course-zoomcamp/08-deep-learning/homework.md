## Homework

### Dataset

For this homework, we will use well known dataset for image classification "Dogs&Cats" that can be downloaded from 
[Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data)

Main goal for the homework is to be able to predict the exact class (label) of the certain image (whether it's a dog or cat displayed in this image).

### Data Preparation

You will need to work with the data that is stored in `'train'` folder. There you can find 12500 images of cats and 12500 images of dogs. 
Before start doing the tasks you need to perform following steps:

* Create two (empty) folders in `'train'` folder and call them, for example `'cats'` and `'dogs'`
* Put all the images of cats and dogs in these new corresponding folders accordingly
* Create new distinct empty folder(outside `'train'` folder) and call it, for example `'val'`
* Create two (empty) folders in `'val'` folder and call them, for example `'cats'` and `'dogs'`
* Put the images from _10000 to _12499 from `'train'` `'cats'` and `'dogs'` folders to corresponding folders in `'val'`. 

After these steps, you will have 20000 images in `'train'` folder (from _0 to _9999) and 5000 images in `'val'` folder (from _10000 to _12499)

These steps can be done manually or from the code (`os` and `shutil` libraries can be used)

### Model

For this homework we will use Convolutional Neural Network (CNN), that will be implemented using Keras framework.

You need to develop the model with following structure:

* Input shape should be (150, 150, 3)
* Conv2D layer with 32 filters, (3,3) strides and 'relu' as activation function
* MaxPooling2D (2,2) layer
* Dense layer with 64 neurons
* Output layer: Dense layer with 1 neuron

As optimizer please use SGD with the following parameters:

* SGD(lr=0.002, momentum=0.8)

### Question 1

If we have task of image classification (two classes), what is the best loss function for the model?


### Question 2

What's the Total params number of the model? You can use model.summary() function. 


### Generators and Training

For next questions, we will create data generators (without augmentation and with augmentation)

Data Generator without augmentation: 

`ImageDataGenerator(rescale=1./255)`

Data Generator with augmentation: 

`ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')`
    
For training use `.fit_generator()` with the following params:

`model.fit_generator(
    train_generator,
    steps_per_epoch=100,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=50)`

### Question 3

What is the median of training accuracy for non-augmented model? (use `history` in keras)

### Question 4

What is the standard deviation of training loss for non-augmented model?

### Question 5 

What is the mean of validation loss for augmented model?

### Question 6

What is the standard deviation of validation accuracy for augmented model?

## Submit the results

Submit your results here: 

If your answer doesn't match options exactly, select the closest one.


## Deadline

The deadline for submitting is TBD. After that, the form will be closed.

## Nagivation

TBD
