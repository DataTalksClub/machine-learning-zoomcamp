## Homework

> **Note**: it's very likely that in this homework your answers won't match 
> the options exactly. That's okay and expected. Select the option that's
> closest to your solution.
> If it's exactly in between two options, select the higher value.

### Dataset

In this homework, we'll build a model for classifying various hair types. 
For this, we will use the Hair Type dataset that was obtained from 
[Kaggle](https://www.kaggle.com/datasets/kavyasreeb/hair-type-dataset) 
and slightly rebuilt.

You can download the target dataset for this homework from 
[here](https://github.com/SVizor42/ML_Zoomcamp/releases/download/straight-curly-data/data.zip):

```bash
wget https://github.com/SVizor42/ML_Zoomcamp/releases/download/straight-curly-data/data.zip
unzip data.zip
```

In the lectures we saw how to use a pre-trained neural network. In the homework, we'll train a much smaller model from scratch. 

We will use PyTorch for that.

You can use Google Colab or your own computer for that.

### Data Preparation

The dataset contains around 1000 images of hairs in the separate folders 
for training and test sets. 

### Reproducibility

Reproducibility in deep learning is a multifaceted challenge that requires attention 
to both software and hardware details. In some cases, we can't guarantee exactly the same results during the same experiment runs.

Therefore, in this homework we suggest to set the random number seed generators by:

```python
import numpy as np
import torch

SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed(SEED)
    torch.cuda.manual_seed_all(SEED)

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

Also, use PyTorch of version 2.8.0 (that's the one in Colab).

### Model

For this homework we will use Convolutional Neural Network (CNN). We'll use PyTorch.

You need to develop the model with following structure:

* The shape for input should be `(3, 200, 200)` (channels first format in PyTorch)
* Next, create a convolutional layer (`nn.Conv2d`):
    * Use 32 filters (output channels)
    * Kernel size should be `(3, 3)` (that's the size of the filter)
    * Use `'relu'` as activation 
* Reduce the size of the feature map with max pooling (`nn.MaxPool2d`)
    * Set the pooling size to `(2, 2)`
* Turn the multi-dimensional result into vectors using `flatten` or `view`
* Next, add a `nn.Linear` layer with 64 neurons and `'relu'` activation
* Finally, create the `nn.Linear` layer with 1 neuron - this will be the output
    * The output layer should have an activation - use the appropriate activation for the binary classification case

As optimizer use `torch.optim.SGD` with the following parameters:

* `torch.optim.SGD(model.parameters(), lr=0.002, momentum=0.8)`


### Question 1

Which loss function you will use?

* `nn.MSELoss()`
* `nn.BCEWithLogitsLoss()`
* `nn.CrossEntropyLoss()`
* `nn.CosineEmbeddingLoss()`

(Multiple answered can be correct, so pick any)


### Question 2

What's the total number of parameters of the model? You can use `torchsummary` or count manually. 

In PyTorch, you can find the total number of parameters using:

```python
# Option 1: Using torchsummary (install with: pip install torchsummary)
from torchsummary import summary
summary(model, input_size=(3, 200, 200))

# Option 2: Manual counting
total_params = sum(p.numel() for p in model.parameters())
print(f"Total parameters: {total_params}")
```

* 896 
* 11214912
* 15896912
* 20073473

### Generators and Training

For the next two questions, use the following transformation for both train and test sets:

```python
train_transforms = transforms.Compose([
    transforms.Resize((200, 200)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ) # ImageNet normalization
])
```

* We don't need to do any additional pre-processing for the images.
* Use `batch_size=20`
* Use `shuffle=True` for both training, but `False` for test. 

Now fit the model.

You can use this code:

```python
num_epochs = 10
history = {'acc': [], 'loss': [], 'val_acc': [], 'val_loss': []}

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    correct_train = 0
    total_train = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        labels = labels.float().unsqueeze(1) # Ensure labels are float and have shape (batch_size, 1)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        # For binary classification with BCEWithLogitsLoss, apply sigmoid to outputs before thresholding for accuracy
        predicted = (torch.sigmoid(outputs) > 0.5).float()
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()

    epoch_loss = running_loss / len(train_dataset)
    epoch_acc = correct_train / total_train
    history['loss'].append(epoch_loss)
    history['acc'].append(epoch_acc)

    model.eval()
    val_running_loss = 0.0
    correct_val = 0
    total_val = 0
    with torch.no_grad():
        for images, labels in validation_loader:
            images, labels = images.to(device), labels.to(device)
            labels = labels.float().unsqueeze(1)

            outputs = model(images)
            loss = criterion(outputs, labels)

            val_running_loss += loss.item() * images.size(0)
            predicted = (torch.sigmoid(outputs) > 0.5).float()
            total_val += labels.size(0)
            correct_val += (predicted == labels).sum().item()

    val_epoch_loss = val_running_loss / len(validation_dataset)
    val_epoch_acc = correct_val / total_val
    history['val_loss'].append(val_epoch_loss)
    history['val_acc'].append(val_epoch_acc)

    print(f"Epoch {epoch+1}/{num_epochs}, "
          f"Loss: {epoch_loss:.4f}, Acc: {epoch_acc:.4f}, "
          f"Val Loss: {val_epoch_loss:.4f}, Val Acc: {val_epoch_acc:.4f}"))
```

### Question 3

What is the median of training accuracy for all the epochs for this model?

* 0.05
* 0.12
* 0.40
* 0.84

### Question 4

What is the standard deviation of training loss for all the epochs for this model?

* 0.007
* 0.078
* 0.171
* 1.710


### Data Augmentation

For the next two questions, we'll generate more data using data augmentations. 

Add the following augmentations to your training data generator:

```python
transforms.RandomRotation(50),
transforms.RandomResizedCrop(200, scale=(0.9, 1.0), ratio=(0.9, 1.1)),
transforms.RandomHorizontalFlip(),
```

### Question 5 

Let's train our model for 10 more epochs using the same code as previously.

> **Note:** make sure you don't re-create the model.
> we want to continue training the model we already started training.

What is the mean of test loss for all the epochs for the model trained with augmentations?

* 0.008
* 0.08
* 0.88
* 8.88

### Question 6

What's the average of test accuracy for the last 5 epochs (from 6 to 10)
for the model trained with augmentations?

* 0.08
* 0.28
* 0.68
* 0.98

## Submit the results

* Submit your results here: https://courses.datatalks.club/ml-zoomcamp-2025/homework/hw08
* If your answer doesn't match options exactly, select the closest one. If the answer is exactly in between two options, select the higher value.
