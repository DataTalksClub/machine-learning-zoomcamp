# Deep Learning with PyTorch Workshop


* [Video](https://www.youtube.com/watch?v=Ne25VujHRLA)
* [Notebook](https://colab.research.google.com/drive/1nCA4Q0f8DVFiLpfXdXvZtYUh-yYDy5i_?usp=sharing)


This workshop introduces deep learning for image classification using PyTorch. It is based on the [ML Zoomcamp Deep Learning module (08-deep-learning)](..) but adapted to use PyTorch instead of TensorFlow/Keras.

Before preparing this workshop, I asked Gemini (inside Google Colab) to translate my Keras code into PyTorch and [this is what happened](https://colab.research.google.com/drive/1_kvvbi_msBuTFkkdLxMEpB3mj-Jhh-Bc?usp=sharing). This workshop is based on the code from this notebook.

## Workshop Overview

In this workshop, you will learn how to build an image classification model using PyTorch and transfer learning. We'll work with a clothing dataset and progressively improve our model through experimentation and optimization.

## Plan

- Introduction to PyTorch for deep learning
- Loading and preprocessing image data
- Using pre-trained models (MobileNetV2)
- Understanding convolutional neural networks (CNNs)
- Transfer learning: adapting pre-trained models
- Hyperparameter tuning: learning rate optimization
- Model checkpointing: saving the best model
- Adding more layers to improve performance
- Dropout regularization to prevent overfitting
- Data augmentation for better generalization
- Training the final model
- Using the model for predictions
- Exporting models to ONNX format

## Prerequisites

Tools:

- PyTorch
- torchvision
- PIL (Pillow)
- NumPy

## Setup

We will use Google Colab, so no setup (like installing libraries or CUDA) is required. 

Download the dataset:

```bash
git clone https://github.com/alexeygrigorev/clothing-dataset-small.git
```

The dataset contains:
- 10 clothing categories (dress, hat, longsleeve, outwear, pants, shirt, shoes, shorts, skirt, t-shirt)
- Training, validation, and test splits
- Pre-organized directory structure


## 1. Introduction to PyTorch

PyTorch is a popular open-source deep learning framework developed by Facebook's AI Research lab. It provides:
- Dynamic computation graphs (define-by-run)
- Pythonic API
- Strong GPU acceleration
- Rich ecosystem of tools and libraries

Key Differences from TensorFlow/Keras:

| TensorFlow/Keras | PyTorch |
|------------------|---------|
| `model.fit()` | Manual training loop |
| `ImageDataGenerator` | `Dataset` + `DataLoader` + `transforms` |
| `keras.layers.Dense()` | `nn.Linear()` |
| `keras.Model` | `nn.Module` |
| `.h5` or `.keras` files | `.pth` or `.pt` files |

## 2. PyTorch and Image Loading

PyTorch is a popular open-source deep learning framework developed by Facebook's AI Research lab.

Key differences from TensorFlow/Keras:
- Dynamic computation graphs (define-by-run)
- More Pythonic and flexible
- Manual training loops instead of `model.fit()`
- Explicit device management (CPU/GPU)

### Loading and Preprocessing Images

Images are represented as 3D arrays:
- Height × Width × Channels
- Channels: RGB (Red, Green, Blue)
- Each channel: 8 bits (0-255 values)

```python
from PIL import Image
import numpy as np

# Load an image
img = Image.open('clothing-dataset-small/train/pants/0098b991-e36e-4ef1-b5ee-4154b21e2a92.jpg')

# Resize to target size
img = img.resize((224, 224))

# Convert to numpy array
x = np.array(img)
print(x.shape)  # (224, 224, 3)
```

## 3. Pre-trained Models

Instead of training from scratch, we'll use a model pre-trained on ImageNet (1.4M images, 1000 classes).

Why use pre-trained models?

- Already learned to recognize edges, textures, shapes
- Saves training time
- Works well even with small datasets
- Better performance than training from scratch

### Using MobileNetV2

We'll use MobileNetV2 (in the original tutorial we used Xception):

```python
import torch
import torchvision.models as models
from torchvision import transforms
import numpy as np

# Load pre-trained model
model = models.mobilenet_v2(weights='IMAGENET1K_V1')
model.eval()

# Preprocessing for MobileNetV2
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```

Now do the prediction:

```python
img = Image.open('clothing-dataset-small/train/pants/0098b991-e36e-4ef1-b5ee-4154b21e2a92.jpg')
img_t = preprocess(img)
batch_t = torch.unsqueeze(img_t, 0)

# Make prediction
with torch.no_grad():
    output = model(batch_t)

# Get top predictions
_, indices = torch.sort(output, descending=True)
```

Let's see what's inside:

```python
!wget https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt -O imagenet_classes.txt

# Load ImageNet class names
with open("imagenet_classes.txt", "r") as f:
    categories = [s.strip() for s in f.readlines()]

# Get top 5 predictions
top5_indices = indices[0, :5].tolist()
top5_classes = [categories[i] for i in top5_indices]

print("Top 5 predictions:")
for i, class_name in enumerate(top5_classes):
    print(f"{i+1}: {class_name}")
```

Key concepts:
- Input size: MobileNetV2 expects 224×224 images (Xception uses 299×299)
- Normalization: Images scaled with ImageNet mean and std
- Batch size: Number of images processed together
- Batch dimension: Shape (batch_size, channels, height, width) - e.g., (1, 3, 224, 224)


## 4. Convolutional Neural Networks

Convolutional Neural Networks (CNNs) are specialized neural networks for processing grid-like data such as images.

Key Components:

1. Convolutional Layer: Extracts features using filters
   - Applies filters (e.g., 3×3, 5×5) to detect patterns
   - Creates feature maps (one per filter)
   - Detects edges, textures, shapes

2. ReLU Activation: Introduces non-linearity
   - `f(x) = max(0, x)`
   - Sets negative values to 0
   - Helps network learn complex patterns

3. Pooling Layer: Down-samples feature maps
   - Reduces spatial dimensions
   - Max pooling: takes maximum value in a region
   - Makes features more robust to small translations

4. Fully Connected (Dense) Layer: Final classification
   - Flattens 2D feature maps to 1D vector
   - Connects to output classes

CNN Workflow:
```
Input Image → Conv + ReLU → Pooling → Conv + ReLU → Pooling → Flatten → Dense → Output
```

## 5. Transfer Learning

Transfer Learning reuses a model trained on one task (ImageNet) for a different task (clothing classification).

Approach:

1. Load pre-trained model (feature extractor)
2. Remove original classification head
3. Freeze convolutional layers
4. Add custom layers for our task
5. Train only the new layers

### Custom Dataset Class

First, create a PyTorch `Dataset` to load images:

```python
import os
from torch.utils.data import Dataset
from PIL import Image

class ClothingDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []
        self.classes = sorted(os.listdir(data_dir))
        self.class_to_idx = {cls: i for i, cls in enumerate(self.classes)}

        for label_name in self.classes:
            label_dir = os.path.join(data_dir, label_name)
            for img_name in os.listdir(label_dir):
                self.image_paths.append(os.path.join(label_dir, img_name))
                self.labels.append(self.class_to_idx[label_name])

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label
```

### Simple Preprocessing

```python
from torchvision import transforms

input_size = 224

# ImageNet normalization values
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

# Simple transforms - just resize and normalize
train_transforms = transforms.Compose([
    transforms.Resize((input_size, input_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])

val_transforms = transforms.Compose([
    transforms.Resize((input_size, input_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])
```

### Create DataLoaders

```python
from torch.utils.data import DataLoader

train_dataset = ClothingDataset(
    data_dir='./clothing-dataset-small/train',
    transform=train_transforms
)

val_dataset = ClothingDataset(
    data_dir='./clothing-dataset-small/validation',
    transform=val_transforms
)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
```

### Build the Model

```python
import torch.nn as nn
import torchvision.models as models

class ClothingClassifierMobileNet(nn.Module):
    def __init__(self, num_classes=10):
        super(ClothingClassifierMobileNet, self).__init__()
        
        # Load pre-trained MobileNetV2
        self.base_model = models.mobilenet_v2(weights='IMAGENET1K_V1')
        
        # Freeze base model parameters
        for param in self.base_model.parameters():
            param.requires_grad = False
        
        # Remove original classifier
        self.base_model.classifier = nn.Identity()
        
        # Add custom layers
        self.global_avg_pooling = nn.AdaptiveAvgPool2d((1, 1))
        self.output_layer = nn.Linear(1280, num_classes)

    def forward(self, x):
        x = self.base_model.features(x)
        x = self.global_avg_pooling(x)
        x = torch.flatten(x, 1)
        x = self.output_layer(x)
        return x
```

### Train the Model

```python
import torch
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = ClothingClassifierMobileNet(num_classes=10)
model.to(device)

optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()
```

Now train it:

```python
# Training loop
num_epochs = 10

for epoch in range(num_epochs):
    # Training phase
    model.train()  # Set the model to training mode
    running_loss = 0.0
    correct = 0
    total = 0

    # Iterate over the training data
    for inputs, labels in train_loader:
        # Move data to the specified device (GPU or CPU)
        inputs, labels = inputs.to(device), labels.to(device)

        # Zero the parameter gradients to prevent accumulation
        optimizer.zero_grad()
        # Forward pass
        outputs = model(inputs)
        # Calculate the loss
        loss = criterion(outputs, labels)
        # Backward pass and optimize
        loss.backward()
        optimizer.step()

        # Accumulate training loss
        running_loss += loss.item()
        # Get predictions
        _, predicted = torch.max(outputs.data, 1)
        # Update total and correct predictions
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    # Calculate average training loss and accuracy
    train_loss = running_loss / len(train_loader)
    train_acc = correct / total

    # Validation phase
    model.eval()  # Set the model to evaluation mode
    val_loss = 0.0
    val_correct = 0
    val_total = 0

    # Disable gradient calculation for validation
    with torch.no_grad():
        # Iterate over the validation data
        for inputs, labels in val_loader:
            # Move data to the specified device (GPU or CPU)
            inputs, labels = inputs.to(device), labels.to(device)
            # Forward pass
            outputs = model(inputs)
            # Calculate the loss
            loss = criterion(outputs, labels)

            # Accumulate validation loss
            val_loss += loss.item()
            # Get predictions
            _, predicted = torch.max(outputs.data, 1)
            # Update total and correct predictions
            val_total += labels.size(0)
            val_correct += (predicted == labels).sum().item()

    # Calculate average validation loss and accuracy
    val_loss /= len(val_loader)
    val_acc = val_correct / val_total

    # Print epoch results
    print(f'Epoch {epoch+1}/{num_epochs}')
    print(f'  Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}')
    print(f'  Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}')
```

It's a lower-level framework, that's why we need to implement some of these things like calculating accuracy on validation.

The line `optimizer.zero_grad()` is crucial in the training loop.

In PyTorch, gradients are accumulated by default. This means that if you don't zero the gradients before calculating the gradients for the current batch, the gradients from the previous batch will be added to the gradients of the current batch. This would lead to incorrect updates to your model's parameters.

By calling `optimizer.zero_grad()`, you clear out the old gradients, ensuring that the gradients calculated during the `loss.backward()` call are only based on the current batch of data. This is essential for the optimizer to take the correct step during `optimizer.step()`.

`model.train()` and `model.eval()` are needed to manage the behavior of certain layers during training and evaluation.

`model.train()` sets the model to training mode. In training mode, layers like Dropout and BatchNorm behave differently. Dropout layers are active (randomly dropping neurons), and BatchNorm layers update their running statistics (mean and variance) based on the current batch.

`model.eval()` sets the model to evaluation mode. In evaluation mode, Dropout layers are inactive (they pass through all neurons), and BatchNorm layers use their accumulated running statistics instead of the current batch statistics. This ensures consistent behavior during inference and prevents randomness from affecting the evaluation results.


Let's put it inside a function so it's easier for us to call it:


```python
def train_and_evaluate(model, optimizer, train_loader, val_loader, criterion, num_epochs, device):
    for epoch in range(num_epochs):
        # Training phase
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        train_loss = running_loss / len(train_loader)
        train_acc = correct / total

        # Validation phase
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0

        with torch.no_grad():
            for inputs, labels in val_loader:
                inputs, labels = inputs.to(device), labels.to(device)

                outputs = model(inputs)
                loss = criterion(outputs, labels)

                val_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                val_total += labels.size(0)
                val_correct += (predicted == labels).sum().item()

        val_loss /= len(val_loader)
        val_acc = val_correct / val_total

        print(f'Epoch {epoch+1}/{num_epochs}')
        print(f'  Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}')
        print(f'  Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}')
```

## 6. Tuning the Learning Rate

The learning rate controls how much to update model weights during training. It's one of the most important hyperparameters.

Analogy: Reading speed
- Too fast: Skip details, poor understanding (may not converge)
- Too slow: Never finish the book (training takes too long)
- Just right: Good comprehension and efficiency

Experimentation approach:

1. Try multiple values: `[0.0001, 0.001, 0.01, 0.1]`
2. Train for a few epochs each
3. Compare validation accuracy
4. Choose the rate with best performance and smallest train/val gap

```python
def make_model(learning_rate=0.01):
    model = ClothingClassifierMobileNet(num_classes=10)
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    return model, optimizer
```

Let's test different learning rates:

```python
learning_rates = [0.0001, 0.001, 0.01, 0.1]

for lr in learning_rates:
    print(f'\n=== Learning Rate: {lr} ===')
    model, optimizer = make_model(learning_rate=lr)
    train_and_evaluate(model, optimizer, train_loader, val_loader, criterion, num_epochs, device)
```

The best learning rate is 0.001 (accuracy 0.815).

## 7. Model Checkpointing

Checkpointing saves the model during training to:
- Keep the best performing model
- Resume training if interrupted
- Avoid losing progress

Update the train function:

```python
def train_and_evaluate_with_checkpointing(model, optimizer, train_loader, val_loader, criterion, num_epochs, device):
    best_val_accuracy = 0.0  # Initialize variable to track the best validation accuracy

    # exising code
    # Checkpoint the model if validation accuracy improved
    if val_acc > best_val_accuracy:
        best_val_accuracy = val_acc
        checkpoint_path = f'mobilenet_v2_{epoch+1:02d}_{val_acc:.3f}.pth'
        torch.save(model.state_dict(), checkpoint_path)
        print(f'Checkpoint saved: {checkpoint_path}')
```

TensorFlow/Keras equivalent:
- Keras: `ModelCheckpoint` callback
- PyTorch: Manual saving in training loop

## 8. Adding Inner Layers

We can add intermediate dense layers between feature extraction and output:

```python
class ClothingClassifierMobileNet(nn.Module):
    def __init__(self, size_inner=100, num_classes=10):
        super(ClothingClassifierMobileNet, self).__init__()
        
        self.base_model = models.mobilenet_v2(weights='IMAGENET1K_V1')
        
        for param in self.base_model.parameters():
            param.requires_grad = False
        
        self.base_model.classifier = nn.Identity()
        
        self.global_avg_pooling = nn.AdaptiveAvgPool2d((1, 1))
        self.inner = nn.Linear(1280, size_inner)  # New inner layer
        self.relu = nn.ReLU()
        self.output_layer = nn.Linear(size_inner, num_classes)

    def forward(self, x):
        x = self.base_model.features(x)
        x = self.global_avg_pooling(x)
        x = torch.flatten(x, 1)
        x = self.inner(x)
        x = self.relu(x)
        x = self.output_layer(x)
        return x
```

Update `make_model`:

```python
def make_model(learning_rate=0.001, size_inner=100):
    model = ClothingClassifierMobileNet(
        num_classes=10,
        size_inner=size_inner
    )
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    return model, optimizer
```

Experiment with different sizes:
- Try: `size_inner = [10, 100, 1000]`
- Larger layers: more capacity, may overfit
- Smaller layers: faster, may underfit

Key points:
- Inner layer uses ReLU activation
- Output layer has no activation (logits)
- `CrossEntropyLoss` applies softmax internally

## 9. Dropout Regularization

Dropout randomly drops neurons during training to prevent overfitting.

How it works:
- Training: randomly set fraction of activations to 0
- Inference: use all neurons (dropout disabled automatically)
- Creates ensemble effect

Benefits:
- Prevents relying on specific features
- Forces learning robust patterns
- Reduces overfitting

```python
class ClothingClassifierMobileNet(nn.Module):
    def __init__(self, size_inner=100, droprate=0.2, num_classes=10):
        super(ClothingClassifierMobileNet, self).__init__()
        
        self.base_model = models.mobilenet_v2(weights='IMAGENET1K_V1')
        
        for param in self.base_model.parameters():
            param.requires_grad = False
        
        self.base_model.classifier = nn.Identity()
        
        self.global_avg_pooling = nn.AdaptiveAvgPool2d((1, 1))
        self.inner = nn.Linear(1280, size_inner)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(droprate)  # Add dropout
        self.output_layer = nn.Linear(size_inner, num_classes)

    def forward(self, x):
        x = self.base_model.features(x)
        x = self.global_avg_pooling(x)
        x = torch.flatten(x, 1)
        x = self.inner(x)
        x = self.relu(x)
        x = self.dropout(x)  # Apply dropout
        x = self.output_layer(x)
        return x
```

Update our function:

```python
def make_model(
        learning_rate=0.001,
        size_inner=100,
        droprate=0.2
):
    model = ClothingClassifierMobileNet(
        num_classes=10,
        size_inner=size_inner,
        droprate=droprate
    )
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    return model, optimizer
```

Experimentation:
- Try: `droprate = [0.0, 0.2, 0.5, 0.8]`
- Typical values: 0.2 to 0.5
- Higher dropout may need more training epochs

(Our case: best droprate is 0.2)

## 10. Data Augmentation

Data Augmentation artificially increases dataset size by applying random transformations to training images.

Common transformations:
- Rotation
- Horizontal/vertical flipping
- Zooming (random cropping)
- Shifting
- Shearing

Important rules:
- ✅ Apply ONLY to training data
- ❌ Never augment validation/test data

### Augmented Training Transforms

```python
# Training transforms WITH augmentation
train_transforms = transforms.Compose([
    transforms.RandomRotation(10),           # Rotate up to 10 degrees
    transforms.RandomResizedCrop(224, scale=(0.9, 1.0)),  # Zoom
    transforms.RandomHorizontalFlip(),       # Horizontal flip
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])

# Validation transforms - NO augmentation, same as before
val_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])
```

When to use augmentation:
1. Small datasets
2. Risk of overfitting
3. Images can appear in different orientations

Tips:
- Choose augmentations that make sense for your data
- Too much augmentation can hurt performance
- Usually requires longer training (more epochs)
- If no improvement after ~20 epochs, don't use it


## 11. Using the Trained Model

### Loading a Saved Model

```python
import glob

# Find best checkpoint
list_of_files = glob.glob('mobilenet_v2_*.pth')
latest_file = max(list_of_files, key=os.path.getctime)
print(f"Loading model from: {latest_file}")

# Load model
model = ClothingClassifierMobileNet(size_inner=32, droprate=0.2, num_classes=10)
model.load_state_dict(torch.load(latest_file))
model.to(device)
model.eval()
```

### Making Predictions

```python
from keras_image_helper import create_preprocessor
import numpy as np

def preprocess_pytorch_style(X):
    # X: shape (1, 224, 224, 3), dtype=float32, values in [0, 255]
    X = X / 255.0
    
    mean = np.array([0.485, 0.456, 0.406]).reshape(1, 3, 1, 1)
    std = np.array([0.229, 0.224, 0.225]).reshape(1, 3, 1, 1)
    
    # Convert NHWC → NCHW (batch, height, width, channels → batch, channels, height, width)
    X = X.transpose(0, 3, 1, 2)
    
    # Normalize
    X = (X - mean) / std
    
    return X.astype(np.float32)

preprocessor = create_preprocessor(preprocess_pytorch_style, target_size=(224, 224))

# Predict from URL
url = 'http://bit.ly/mlbookcamp-pants'
X = preprocessor.from_url(url)
X = torch.Tensor(X).to(device)

with torch.no_grad():
    pred = model(X).cpu().numpy()[0]

classes = [
    "dress", "hat", "longsleeve", "outwear", "pants",
    "shirt", "shoes", "shorts", "skirt", "t-shirt"
]

result = dict(zip(classes, pred.tolist()))
print(result)
```

## 12. Exporting to ONNX

ONNX (Open Neural Network Exchange) is a format for model interoperability.

Benefits:
- Deploy on different platforms
- Use optimized runtimes (ONNX Runtime)
- Better inference performance
- Language-agnostic deployment

```python
# Create dummy input
dummy_input = torch.randn(1, 3, 224, 224).to(device)

# Export to ONNX
onnx_path = "clothing_classifier_mobilenet_v2.onnx"

torch.onnx.export(
    model,
    dummy_input,
    onnx_path,
    verbose=True,
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={
        'input': {0: 'batch_size'},
        'output': {0: 'batch_size'}
    }
)

print(f"Model exported to {onnx_path}")
```

We will use it in the Serverless module.

## Summary

## TensorFlow/Keras vs PyTorch Quick Reference

| Concept | TensorFlow/Keras | PyTorch |
|---------|------------------|---------|
| Framework | High-level API (Keras) on TensorFlow | Low-level, explicit control |
| Data Loading | `ImageDataGenerator` | `Dataset` + `DataLoader` |
| Transforms | `preprocessing_function` | `transforms.Compose()` |
| Model | Functional API or Sequential | `nn.Module` class |
| Layers | `keras.layers.Dense()` | `nn.Linear()` |
| Training | `model.fit()` | Manual training loop |
| Loss | `CategoricalCrossentropy` | `CrossEntropyLoss` |
| Optimizer | `keras.optimizers.Adam` | `optim.Adam` |
| Saving | `.h5` or `.keras` | `.pth` or `.pt` |
| Checkpointing | `ModelCheckpoint` callback | Manual in training loop |
| Device | Automatic | Explicit `.to(device)` |

## Key Concepts Learned

1. Transfer Learning: Reuse pre-trained models for new tasks
2. CNN Architecture: Conv layers → Pooling → Dense layers
3. Hyperparameter Tuning: Learning rate is critical
4. Regularization: Dropout prevents overfitting
5. Data Augmentation: Increases effective dataset size
6. Model Checkpointing: Save best models during training
7. PyTorch Workflow: Dataset → DataLoader → Model → Training Loop

## Best Practices

1. Start with pre-trained models (transfer learning)
2. Freeze convolutional layers initially
3. Use appropriate normalization (match pre-training)
4. Experiment with one hyperparameter at a time
5. Monitor train/val gap for overfitting
6. Use checkpointing to save best models
7. Augment training data only, not validation
8. Train longer with dropout and augmentation
9. Use GPU when available: `torch.cuda.is_available()`

## Next Steps

- Try different pre-trained models (ResNet, EfficientNet)
- Experiment with learning rate schedulers
- Fine-tune the entire model (unfreeze convolutional layers)
- Try different optimizers (SGD with momentum, AdamW)
- Deploy the ONNX model (see [mlzoomcamp-serverless](../mlzoomcamp-serverless/))
- Explore the original [TensorFlow/Keras version](08-deep-learning/)

## Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [torchvision Models](https://pytorch.org/vision/stable/models.html)
- [ML Zoomcamp Course](https://github.com/DataTalksClub/machine-learning-zoomcamp)
- [Original Tutorial (TensorFlow/Keras)](08-deep-learning/)
- [ONNX Documentation](https://onnx.ai/)

## Credits

This workshop is based on the ML Zoomcamp Deep Learning module by [Alexey Grigorev](https://github.com/alexeygrigorev), adapted to use PyTorch instead of TensorFlow/Keras.

