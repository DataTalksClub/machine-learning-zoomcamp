"""Render the exact deep-learning lesson plots at publication resolution.

The values below are copied from the lesson notebook outputs in
``../notebook.ipynb``.  This is intentionally deterministic: these assets are
plots, not conceptual artwork, so imagegen would risk changing the curves or
labels.  The original JPGs and bounded crops remain in this directory as
source evidence.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).parent
EPOCHS_10 = np.arange(10)
EPOCHS_30 = np.arange(30)


LEARNING_RATE = {
    "0.0001": {
        "train": [0.3403, 0.5613, 0.6463, 0.6858, 0.7141, 0.7376, 0.7565, 0.7637, 0.7757, 0.7806],
        "val": [0.4897, 0.6012, 0.6716, 0.7214, 0.7566, 0.7713, 0.7801, 0.7830, 0.7859, 0.7889],
    },
    "0.001": {
        "train": [0.6199, 0.7761, 0.8230, 0.8553, 0.8820, 0.9029, 0.9153, 0.9316, 0.9426, 0.9505],
        "val": [0.7625, 0.8035, 0.8094, 0.8035, 0.8152, 0.8270, 0.8152, 0.8006, 0.8299, 0.8240],
    },
    "0.01": {
        "train": [0.6701, 0.8129, 0.8902, 0.9273, 0.9423, 0.9205, 0.9615, 0.9743, 0.9791, 0.9817],
        "val": [0.7390, 0.7771, 0.7947, 0.7859, 0.7713, 0.8123, 0.8094, 0.8123, 0.8211, 0.7889],
    },
    "0.1": {
        "train": [0.6327, 0.7744, 0.8387, 0.8625, 0.8814, 0.9016, 0.9185, 0.9211, 0.9400, 0.9475],
        "val": [0.7537, 0.7566, 0.7683, 0.7507, 0.7507, 0.7654, 0.7566, 0.7742, 0.7625, 0.7889],
    },
}


TRANSFER_HISTORY = {
    "train": [0.6698, 0.8188, 0.8885, 0.9244, 0.9475, 0.9707, 0.9703, 0.9661, 0.9876, 0.9876],
    "val": [0.7449, 0.8065, 0.8152, 0.7918, 0.8094, 0.8035, 0.8299, 0.8123, 0.8035, 0.7889],
}


DROPOUT = {
    "0.0": {
        "train": [0.6747, 0.8230, 0.8885, 0.9218, 0.9394, 0.9684, 0.9863, 0.9902, 0.9971, 0.9987, 0.9990, 0.9990, 0.9997, 0.9997, 0.9993, 0.9993, 0.9997, 0.9993, 0.9997, 0.9997, 0.9993, 0.9997, 0.9997, 0.9990, 0.9987, 0.9997, 0.9987, 0.9990, 0.9964, 0.9987],
        "val": [0.7566, 0.7918, 0.8270, 0.8416, 0.8152, 0.8152, 0.8152, 0.8211, 0.8270, 0.8416, 0.8152, 0.8270, 0.8328, 0.8358, 0.8328, 0.8152, 0.8270, 0.8299, 0.8240, 0.8328, 0.8387, 0.8358, 0.8240, 0.8358, 0.8299, 0.8358, 0.8211, 0.8358, 0.8152, 0.8358],
    },
    "0.2": {
        "train": [0.6421, 0.7862, 0.8390, 0.8866, 0.9113, 0.9299, 0.9505, 0.9645, 0.9690, 0.9769, 0.9834, 0.9886, 0.9922, 0.9909, 0.9948, 0.9928, 0.9935, 0.9932, 0.9941, 0.9941, 0.9928, 0.9938, 0.9954, 0.9961, 0.9932, 0.9932, 0.9935, 0.9948, 0.9964, 0.9928],
        "val": [0.8152, 0.7830, 0.8152, 0.8182, 0.8446, 0.8270, 0.8152, 0.8299, 0.8152, 0.8152, 0.8270, 0.8446, 0.8416, 0.8358, 0.8270, 0.8387, 0.8416, 0.8152, 0.8387, 0.8270, 0.8152, 0.8270, 0.8328, 0.8094, 0.8065, 0.8182, 0.8416, 0.8094, 0.8152, 0.8065],
    },
}


def save_figure(filename: str, *, ylim=None, yticks=None):
    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.set_axisbelow(True)
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Accuracy", fontsize=13)
    axis.tick_params(labelsize=11)
    if ylim is not None:
        axis.set_ylim(*ylim)
    if yticks is not None:
        axis.set_yticks(yticks)
    figure.tight_layout()
    figure.savefig(ROOT / filename, format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)


def learning_rate_plots():
    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    for learning_rate, history in LEARNING_RATE.items():
        axis.plot(EPOCHS_10, history["train"], linewidth=2.5, label=learning_rate)
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Training accuracy", fontsize=13)
    axis.set_xticks(EPOCHS_10)
    axis.set_ylim(0.3, 1.02)
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(title="learning rate", fontsize=11, title_fontsize=11)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "06-learning-rate-04-train-accuracy-crisp.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    for learning_rate, history in LEARNING_RATE.items():
        axis.plot(EPOCHS_10, history["val"], linewidth=2.5, label=learning_rate)
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Validation accuracy", fontsize=13)
    axis.set_xticks(EPOCHS_10)
    axis.set_ylim(0.45, 0.85)
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(title="learning rate", fontsize=11, title_fontsize=11)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "06-learning-rate-05-val-accuracy-crisp.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    for learning_rate in ("0.001", "0.01"):
        axis.plot(EPOCHS_10, LEARNING_RATE[learning_rate]["val"], linewidth=2.5, label=learning_rate)
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Validation accuracy", fontsize=13)
    axis.set_xticks(EPOCHS_10)
    axis.set_ylim(0.73, 0.84)
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(title="learning rate", fontsize=11, title_fontsize=11)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "06-learning-rate-06-two-lr-validation-crisp.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    for learning_rate in ("0.001", "0.01"):
        axis.plot(EPOCHS_10, LEARNING_RATE[learning_rate]["train"], linewidth=2.5, label=f"train={learning_rate}")
        axis.plot(EPOCHS_10, LEARNING_RATE[learning_rate]["val"], linewidth=2.5, label=f"val={learning_rate}")
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Accuracy", fontsize=13)
    axis.set_xticks(EPOCHS_10)
    axis.set_ylim(0.73, 1.02)
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(fontsize=11, ncol=2)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "06-learning-rate-07-select-001-crisp.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)


def transfer_plot():
    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    axis.plot(EPOCHS_10, TRANSFER_HISTORY["train"], linewidth=2.5, label="train")
    axis.plot(EPOCHS_10, TRANSFER_HISTORY["val"], linewidth=2.5, label="val")
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Accuracy", fontsize=13)
    axis.set_xticks(EPOCHS_10)
    axis.set_ylim(0.6, 1.02)
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(fontsize=11)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "05-transfer-learning-08-history-plot-crisp.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)


def dropout_plots():
    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    axis.plot(EPOCHS_30 + 1, DROPOUT["0.2"]["val"], linewidth=2.5, label="val=0.2")
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Validation accuracy", fontsize=13)
    axis.set_xlim(1, 30)
    axis.set_ylim(0.78, 0.86)
    axis.set_xticks([1, 5, 10, 15, 20, 25, 30])
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(fontsize=11)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "09-dropout-07-dropout-02-vs-train-imagegen.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(10, 6), dpi=200)
    axis.plot(EPOCHS_30 + 1, DROPOUT["0.0"]["val"], linewidth=2.5, label="val")
    axis.plot(EPOCHS_30 + 1, DROPOUT["0.0"]["train"], linewidth=2.5, label="train")
    axis.set_xlabel("Epoch", fontsize=13)
    axis.set_ylabel("Accuracy", fontsize=13)
    axis.set_xlim(1, 30)
    axis.set_ylim(0.65, 1.02)
    axis.set_xticks([1, 5, 10, 15, 20, 25, 30])
    axis.grid(True, color="#d9dee7", linewidth=0.8, alpha=0.75)
    axis.legend(fontsize=11)
    axis.set_axisbelow(True)
    figure.tight_layout()
    figure.savefig(ROOT / "09-dropout-08-no-regularization-overfit-imagegen.png", format="png", dpi=200, metadata={"Source": "08-deep-learning/notebook.ipynb"})
    plt.close(figure)


if __name__ == "__main__":
    learning_rate_plots()
    transfer_plot()
    dropout_plots()
