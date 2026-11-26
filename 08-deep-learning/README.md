## 8. Neural Networks and Deep Learning

Note: in the module we use TensorFlow+Keras. These videos 
were recorded a while ago, and while they are still
relevant, PyTorch became the to-go framework for training
neural networks. 

That's why we also re-recorded the content of this module
with PyTorch. You can find the materials in the [pytorch/](pytorch/) folder.

We don't go over the theory in the PyTorch part. For that,
refer to the main module (the one that still uses Keras).

How to watch it:

- If you want to learn PyTorch only, watch the module content for the theory only and then follow along the content of the PyTorch part
- If you want to learn both (and have time), first do the module and then the PyTorch part 

TensorFlow module videos:

- 8.1 [Fashion classification](01-fashion-classification.md) - Introduce the fashion classification project, its clothing dataset, and the plan for the deep learning module.
- 8.2 [TensorFlow and Keras](02-tensorflow-keras.md) - Install TensorFlow, import Keras, and load, resize and convert a clothing image into a NumPy array.
- 8.3 [Pre-trained convolutional neural networks](03-pretrained-models.md) - Run a clothing image through the pre-trained Xception model on ImageNet and decode its predictions.
- 8.4 [Convolutional neural networks](04-conv-neural-nets.md) - Explain how convolutional and dense layers turn an image into a vector and then a prediction.
- 8.5 [Transfer learning](05-transfer-learning.md) - Reuse Xception's convolutional layers with a frozen base, a new pooling and dense head, and train it on clothing images.
- 8.6 [Adjusting the learning rate](06-learning-rate.md) - Compare several Adam learning rates on the transfer learning model and select the best one from validation accuracy.
- 8.7 [Checkpointing](07-checkpointing.md) - Save the best model during training with Keras ModelCheckpoint, keeping the epoch with the highest validation accuracy.
- 8.8 [Adding more layers](08-more-layers.md) - Add an inner dense layer with ReLU activation and compare layer sizes of 10, 100 and 1000 on validation accuracy.
- 8.9 [Regularization and dropout](09-dropout.md) - Add a dropout layer to the model and compare dropout rates from 0.0 to 0.8, choosing 0.2 for later units.
- 8.10 [Data augmentation](10-augmentation.md) - Add image augmentation to the training generator only, train for 50 epochs, and review how to choose augmentations.
- 8.11 [Training a larger model](11-large-model.md) - Train the final Xception model on 299x299 images with an inner layer, dropout, light augmentation and a lower learning rate.
- 8.12 [Using the model](12-using-model.md) - Load the saved h5 checkpoint, evaluate it on the test set, and predict the class of one pants image.
- 8.13 [Summary](13-summary.md) - Recap the transfer learning, tuning and checkpointing steps behind the clothing classifier, which reaches about 90% test accuracy.
- 8.14 [Explore more](14-explore-more.md) - Suggest next steps covering more data, Albumentations augmentation, PyTorch, other architectures and other image projects.
- 8.15 [Installation of TensorFlow](15-install.md) - Install a GPU-enabled TensorFlow 2.14 stack on WSL2 with CUDA, cuDNN and micromamba, then verify GPU access.

## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Alvaro Navas' Notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/08_deep_learning.md)
* [Kwang Yang's Notes on PyTorch](https://github.com/kwangyy/ml-zoomcamp/blob/main/Week%208%20Code/Week%208%20-%20Deep%20Learning%20but%20PyTorch.ipynb)
* [Notes from froukje](https://github.com/froukje/ml-zoomcamp/blob/main/week8/Lecture_week_8.ipynb)
* [Saturn Cloud setup](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/saturn.md)
* [Connecting Github, Saturn Cloud and local VSCode via SSH](https://github.com/MemoonaTahira/MLZoomcamp2022/tree/main/Notes/Week_8-Deep_Learning)
* [Gradio demonstration with Huggingface Space](https://github.com/yusyel/guides/tree/master/huggingface#gradio-demonstration-with-huggingface-space)
* [Hyperparameter Search With Keras-tuners](https://github.com/yusyel/guides/tree/master/keras%20tuner)
* [Installation of tensorflow v2.14 in WSL2 and Ubuntu 22.04 with Nvidia GPU](https://github.com/ellacharmed/machine-learning-zoomcamp/blob/master/08-deep-learning/install.md)
* [Notes from Peter Ernicke](https://knowmledge.com/category/courses/ml-zoomcamp/deep-learning/)
* [Notes from Kemal Dahha](https://github.com/kemaldahha/machine-learning-course/blob/main/week_8_notes.ipynb)
* [Notes from Maximilien Eyengue](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/08_deep_learning/Summary_Session_08.md)
* [Notes from Revathy Ramalingam](https://github.com/RevathyRamalingam/machineLearning/blob/main/08-DeepLearning/README.md)
* Add your notes here
