## Homework 8: Neural Networks and Deep Learning

In this homework we build a small PyTorch model that classifies curly and
straight hair. The 2026 reference setup freezes the dataset, framework
versions, architecture, split, random seed, and evaluation procedure. These
settings make the experiment reproducible while still showing why augmentation
can change a model's behavior.

## Dataset

Download the fixed archive:

```bash
wget https://github.com/SVizor42/ML_Zoomcamp/releases/download/straight-curly-data/data.zip
sha256sum data.zip
unzip -q data.zip
```

The checksum must be:

```text
9e53453e3017502f22860cb08558f0cdb343e102fb61feab75960616185e7d67  data.zip
```

The archive contains a fixed training split and a fixed held-out evaluation
split. It has 1,002 image files. One GIF is kept in the archive for provenance
but `ImageFolder` ignores it, so the training run consumes 1,001 images:

| Split | Curly | Straight | Total |
| --- | ---: | ---: | ---: |
| Train | 410 | 390 | 800 |
| Held-out evaluation | 103 | 98 | 201 |

`torchvision.datasets.ImageFolder` assigns `curly=0` and `straight=1` because
the class directories are sorted alphabetically. Do not create another random
train/test split and do not augment the held-out evaluation images.

## Environment

For the reference run, use Python 3.11 and CPU wheels:

```bash
python -m pip install -r requirements-cpu.txt
```

The important CPU wheels are `torch==2.9.0+cpu` and
`torchvision==0.24.0+cpu`. Also use
`numpy==2.3.3`, and `Pillow==11.3.0`. The CPU reference defines the grading
baseline. You can experiment on a GPU, but report the CPU run for the numeric
questions.

The directory also contains `reference_train.py`. After extracting the archive,
run `python reference_train.py --data-dir data` to produce both history files
with the complete reference procedure.

## Reproducibility rules

Run this before constructing datasets, data loaders, the model, or the
optimizer:

```python
import random

import numpy as np
import torch

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.use_deterministic_algorithms(True)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

device = torch.device("cpu")
```

Use `num_workers=0` for both loaders. Give the training loader its own fixed
generator:

```python
loader_generator = torch.Generator().manual_seed(SEED)
train_loader = DataLoader(
    train_dataset,
    batch_size=20,
    shuffle=True,
    num_workers=0,
    generator=loader_generator,
)
evaluation_loader = DataLoader(
    evaluation_dataset,
    batch_size=20,
    shuffle=False,
    num_workers=0,
)
```

These settings remove the worker-order and GPU/cuDNN differences that made the
2025 scalar answers move between runs.

## Model and preprocessing

Use this transform for the baseline training set and, separately, for the
held-out evaluation set:

```python
from torchvision import transforms

evaluation_transform = transforms.Compose([
    transforms.Resize((200, 200), interpolation=transforms.InterpolationMode.BILINEAR),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    ),
])
```

Create the model with exactly this structure:

```python
import torch.nn as nn


class HairModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=0)
        self.pool = nn.MaxPool2d(kernel_size=2)
        self.hidden = nn.Linear(32 * 99 * 99, 64)
        self.output = nn.Linear(64, 1)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv(x)))
        x = x.flatten(start_dim=1)
        x = nn.functional.relu(self.hidden(x))
        return self.output(x)
```

The model returns logits. Use `nn.BCEWithLogitsLoss()` and apply
`torch.sigmoid` only when calculating predictions or serving the model. Do not
put a sigmoid module in `HairModel` as well; applying it twice was an
ambiguity in the previous assignment.

Use this optimizer and loss:

```python
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.002,
    momentum=0.8,
)
```

## Question 1 — loss and output contract

Which loss matches the model above?

- `nn.MSELoss()`
- `nn.BCEWithLogitsLoss()`
- `nn.CrossEntropyLoss()`
- `nn.CosineEmbeddingLoss()`

There is one intended answer: the model emits one logit and the loss applies the
stable sigmoid-plus-binary-cross-entropy operation.

## Question 2 — parameter count

What is the total number of trainable parameters? Count biases as well and use
`sum(p.numel() for p in model.parameters())`.

- `896`
- `11214912`
- `15896912`
- `20073473`

## Training metrics

Train for 10 epochs with the baseline transform. For every epoch, evaluate the
held-out split with `model.eval()` and `torch.no_grad()`. Store these four
series in a JSON file named `history_baseline.json`:

```python
{
    "train_loss": [...],
    "train_accuracy": [...],
    "evaluation_loss": [...],
    "evaluation_accuracy": [...],
}
```

For accuracy, use `(torch.sigmoid(logits) >= 0.5)`. Use the number of examples,
not the number of batches, when averaging loss and accuracy.

## Question 3 — baseline accuracy

Calculate the median of `train_accuracy` in `history_baseline.json`. Submit the
value rounded to two decimal places. The grader accepts an absolute error of
`0.05`; the answer is not selected from a fixed option list.

## Question 4 — baseline loss

Calculate the population standard deviation of `train_loss` in
`history_baseline.json` (for NumPy, use `np.std(values, ddof=0)`). Submit the
value rounded to three decimal places. The grader accepts an absolute error of
`0.02`.

## Data augmentation

Keep the same model and optimizer. Replace only the training transform with:

```python
train_transform_augmented = transforms.Compose([
    transforms.Resize((200, 200), interpolation=transforms.InterpolationMode.BILINEAR),
    transforms.RandomRotation(
        50,
        interpolation=transforms.InterpolationMode.NEAREST,
    ),
    transforms.RandomResizedCrop(
        200,
        scale=(0.9, 1.0),
        ratio=(0.9, 1.1),
        interpolation=transforms.InterpolationMode.BILINEAR,
    ),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    ),
])
```

Do not recreate the model or optimizer. Train for 10 additional epochs and
write only those ten epochs to `history_augmented.json`. Continue using the
unchanged, deterministic `evaluation_dataset` and `evaluation_loader` for
every evaluation.

## Question 5 — augmented evaluation loss

Calculate the mean of `evaluation_loss` in `history_augmented.json`. Submit the
value rounded to three decimal places. The grader accepts an absolute error of
`0.02`.

## Question 6 — augmented evaluation accuracy

Calculate the mean of the last five values in `evaluation_accuracy` in
`history_augmented.json` (epochs 6 through 10 of the augmented phase). Submit
the value rounded to two decimal places. The grader accepts an absolute error
of `0.05`.

The tolerances cover minor CPU wheel differences, while the fixed seed, loader,
split, architecture, and inference transform prevent the large uncontrolled
variation from the 2025 exercise.

## Submit the results

Submit the results here:
<https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw08>.

Include the two history JSON files or a link to the notebook/script that
produced them. Numeric answers must use the precision and tolerance stated in
each question.
