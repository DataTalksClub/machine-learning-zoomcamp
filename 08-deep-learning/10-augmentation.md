## 8.10 Data augmentation

<a href="https://www.youtube.com/watch?v=aoPfVsS3BDE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-10.jpg"></a>

In this video, I had a typo/bug: instead of using `val_gen` for generating images for validation,
I used `train_gen`. That's why adding augmentations didn't help in the video.

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-8-neural-networks-and-deep-learning-250592316)


Data augmentation is a process of artifically increasing the amount of data by generating new images from existing images. This includes adding minor alterations to images by flipping, cropping, adding brightness and/or contrast, and many more.

Keras `ImageDataGenerator` class has many parameters for data augmentation that we can use for generating data. Important thing to remember that the data augmentation should only be implemented on train data, not the validation. Here's how we can generate augmented data for training the model:

```python
# Create image generator for train data and also augment the images
train_gen = ImageDataGenerator(preprocessing_function=preprocess_input,
                               rotation_range=30,
                               width_shift_range=10.0,
                               height_shift_range=10.0,
                               shear_range=10,
                               zoom_range=0.1,
                               vertical_flip=True)

train_ds = train_gen.flow_from_directory(directory=train_imgs_dir,
                                         target_size=(150,150),
                                         batch_size=32)
```

**How to choose augmentations?**

- First step is to use our own judgement, for example, looking at the images (both on train and validation), does it make sense to introduce horizontal flip?
- Look at the dataset, what kind of variations are there? Are objects always centered?
- Augmentations are hyperparameters: like many other hyperparameters, often times we need to test whether image augmentations are useful for the model or not. If the model doesn't improve or have same performance after certain epochs (let's say 20), in that case we don't use it.

Usually augmented data required training for longer.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/11/27/ml-zoomcamp-2023-deep-learning-part-12/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 8: Neural Networks and Deep Learning](./)
* Previous: [Regularization and dropout](09-dropout.md)
* Next: [Training a larger model](11-large-model.md)
