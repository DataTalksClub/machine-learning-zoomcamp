from __future__ import annotations

import argparse
import json
import random
import statistics
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


SEED = 42
BATCH_SIZE = 20
EPOCHS_PER_PHASE = 10
NORMALIZE = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225],
)


def seed_everything(seed: int = SEED) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


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


def evaluation_transform():
    return transforms.Compose([
        transforms.Resize(
            (200, 200),
            interpolation=transforms.InterpolationMode.BILINEAR,
        ),
        transforms.ToTensor(),
        NORMALIZE,
    ])


def augmented_train_transform():
    return transforms.Compose([
        transforms.Resize(
            (200, 200),
            interpolation=transforms.InterpolationMode.BILINEAR,
        ),
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
        NORMALIZE,
    ])


def make_loader(dataset, *, shuffle: bool, seed: int | None = None):
    options = {
        "batch_size": BATCH_SIZE,
        "shuffle": shuffle,
        "num_workers": 0,
    }
    if seed is not None:
        options["generator"] = torch.Generator().manual_seed(seed)
    return DataLoader(dataset, **options)


def evaluate(model, loader, criterion, device):
    model.eval()
    loss_sum = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            labels = labels.float().unsqueeze(1)
            logits = model(images)
            loss = criterion(logits, labels)
            loss_sum += loss.item() * images.size(0)
            correct += ((torch.sigmoid(logits) >= 0.5) == labels).sum().item()
            total += labels.size(0)
    return loss_sum / total, correct / total


def train_phase(model, loader, evaluation_loader, criterion, optimizer, device):
    history = {
        "train_loss": [],
        "train_accuracy": [],
        "evaluation_loss": [],
        "evaluation_accuracy": [],
    }
    for _ in range(EPOCHS_PER_PHASE):
        model.train()
        loss_sum = 0.0
        correct = 0
        total = 0
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            labels = labels.float().unsqueeze(1)
            optimizer.zero_grad()
            logits = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            loss_sum += loss.item() * images.size(0)
            correct += ((torch.sigmoid(logits) >= 0.5) == labels).sum().item()
            total += labels.size(0)

        evaluation_loss, evaluation_accuracy = evaluate(
            model,
            evaluation_loader,
            criterion,
            device,
        )
        history["train_loss"].append(loss_sum / total)
        history["train_accuracy"].append(correct / total)
        history["evaluation_loss"].append(evaluation_loss)
        history["evaluation_accuracy"].append(evaluation_accuracy)
    return history


def run(data_dir: Path, output_dir: Path) -> None:
    seed_everything()
    torch.set_num_threads(2)
    device = torch.device("cpu")
    train_dir = data_dir / "train"
    evaluation_dir = data_dir / "test"

    baseline_dataset = datasets.ImageFolder(train_dir, transform=evaluation_transform())
    evaluation_dataset = datasets.ImageFolder(
        evaluation_dir,
        transform=evaluation_transform(),
    )
    if len(baseline_dataset) != 800 or len(evaluation_dataset) != 201:
        raise ValueError(
            "unexpected ImageFolder counts; verify the archive against "
            "dataset_manifest.json"
        )
    if baseline_dataset.class_to_idx != {"curly": 0, "straight": 1}:
        raise ValueError(f"unexpected class mapping: {baseline_dataset.class_to_idx}")

    evaluation_loader = make_loader(evaluation_dataset, shuffle=False)
    model = HairModel().to(device)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.002, momentum=0.8)

    baseline = train_phase(
        model,
        make_loader(baseline_dataset, shuffle=True, seed=SEED),
        evaluation_loader,
        criterion,
        optimizer,
        device,
    )
    augmented_dataset = datasets.ImageFolder(
        train_dir,
        transform=augmented_train_transform(),
    )
    augmented = train_phase(
        model,
        make_loader(augmented_dataset, shuffle=True, seed=SEED + 1),
        evaluation_loader,
        criterion,
        optimizer,
        device,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "history_baseline.json").write_text(
        json.dumps(baseline, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "history_augmented.json").write_text(
        json.dumps(augmented, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        "output_dir": str(output_dir),
        "parameters": sum(parameter.numel() for parameter in model.parameters()),
        "baseline_median_train_accuracy": statistics.median(
            baseline["train_accuracy"]
        ),
        "baseline_train_loss_std_population": float(
            np.std(baseline["train_loss"], ddof=0)
        ),
        "augmented_mean_evaluation_loss": statistics.mean(
            augmented["evaluation_loss"]
        ),
        "augmented_last_five_evaluation_accuracy": statistics.mean(
            augmented["evaluation_accuracy"][-5:]
        ),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--output-dir", type=Path, default=Path("runs/reference"))
    args = parser.parse_args()
    run(args.data_dir, args.output_dir)
