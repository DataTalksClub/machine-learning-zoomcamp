# **Complete PyTorch Installation Guide (GPU & CPU Support)**

Hi 👋
This guide walks you through installing PyTorch with GPU acceleration using **uv**, a modern Python package manager. It also shows how to check your GPU, verify your installation, and fix common issues.

Tested on Linux and WSL2.

---

## **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [Step-by-Step Installation](#step-by-step-installation)
   * [Step 1: Check Your Graphics Card](#step-1-check-your-graphics-card)
   * [Step 2: Create an Environment](#step-2-create-an-environment)
   * [Step 3: Install PyTorch](#step-3-install-pytorch)
   * [Step 4: Verify Installation](#step-4-verify-installation)
3. [Troubleshooting Common Issues](#troubleshooting-common-issues)
4. [FAQs](#faqs)

---

## **Prerequisites**

Before installing PyTorch, ensure your system meets the following requirements.

### **System Requirements**

* **OS**: Linux, WSL2 (recommended for Windows), or macOS
* **Shell**: bash, zsh, or similar
* **Python**: 3.10+
* **Memory**: At least 8 GB RAM (16 GB recommended for deep learning)

### **GPU Requirements**

* **NVIDIA GPU** with compute capability ≥ 3.5
* Recent **NVIDIA driver** installed
* **AMD GPUs** supported via ROCm (check compatibility)
* Integrated graphics are fine for CPU-only, but not recommended for serious training

---

## **Step-by-Step Installation**

### **Step 1: Check Your Graphics Card**

First, identify your GPU and the maximum CUDA version your driver supports.

```bash
nvidia-smi
```

Example output (shortened):

```shell
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08   Driver Version: 580.105.08   CUDA Version: 13.0     |
|   0  NVIDIA GeForce GTX 1650         On | 00000000:01:00.0 On |         N/A |
+-----------------------------------------------------------------------------+
```

Key information to note:

* **Driver Version**
* **CUDA Version** (this is the *maximum* supported)
* **GPU Model**

> 💡 **Note:** PyTorch ships its own CUDA runtime – you do **not** need to install the system CUDA toolkit just to use PyTorch.

Optional: check compute capability:

```bash
nvidia-smi --query-gpu=compute_cap --format=csv
```

> 💡 **Note:** For the AMD versions, there is a similar command `amd-smi`, to accomplish the same effect as the NVIDIA system.
---

## **Step 2: Create an Environment**

PyTorch should always be installed inside a **dedicated environment** to avoid dependency conflicts and keep your system clean.

During the seminar, we used **uv**, a fast modern Python package manager.

### **Install uv**

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### **Create and activate an isolated environment**

```bash
uv venv pytorch-env
source pytorch-env/bin/activate     # Linux/macOS
.\pytorch-env\Scripts\activate      # Windows
```

Your environment is now ready for the PyTorch installation step.

---

## **Step 3: Install PyTorch**

This is the core of the guide: choosing the **right PyTorch build** and installing it with `uv`.

PyTorch offers several flavours:

* **CUDA builds** (for NVIDIA GPUs)
* **CPU-only builds** (no GPU required)
* **ROCm builds** (for supported AMD GPUs)

> **Recommendation:** Use the newest PyTorch CUDA version that is **≤ the CUDA version** shown by `nvidia-smi`. For most users, **CUDA 12.8** is the best, stable choice.

### **3.1 Choose your build**

Use this decision flow:

* **You have an NVIDIA GPU and want GPU acceleration**
  → Use the **CUDA 12.8 build**.

* **You do not have a dedicated GPU / just want CPU**
  → Use the **CPU-only build**.

* **You have a supported AMD GPU**
  → Use the **ROCm build** (check your model in AMD’s ROCm compatibility list).

You can always check other combinations on the official PyTorch install page:
[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

### **3.2 Install with uv**

All commands below assume your `uv` environment is already activated.

#### **Install PyTorch (CUDA 12.8 — recommended)**

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

This installs:

* `torch` (PyTorch core)
* `torchvision` (vision utilities and models)
* `torchaudio` (audio utilities)

> **Other variants:**
>
> * **CPU-only:** replace `cu128` with `cpu`
> * **AMD ROCm:** replace `cu128` with `rocm6.4`
> * **Nightly build:** replace `download.pytorch.org/whl` with `download.pytorch.org/whl/nightly`
>   Example for nightly CUDA 12.8:
>
>   ```bash
>   uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
>   ```
>
> Check the PyTorch website for all supported builds.

---

## **Step 4: Verify Installation**

Run this one-liner to confirm that PyTorch is installed and can see your GPU:

```bash
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

If `CUDA available: True`, your GPU build is working.

---

## **Troubleshooting Common Issues**

### **CUDA not available**

1. Check `nvidia-smi` detects your GPU
2. Make sure you installed a **CUDA-enabled (cuXXX)** build, not CPU-only
3. Update your NVIDIA driver to a recent version

### **Out-of-memory errors (OOM)**

* Reduce batch size
* Use mixed precision (`torch.cuda.amp`)
* Close other GPU-heavy applications

### **Python version issues**

* If you encounter installation errors, recreate your `uv` environment with a **supported Python version** (e.g., 3.10 or 3.11).
* Avoid the **very latest** Python release, as PyTorch support often lags behind new versions.
* Downgrading Python is a valid and common solution when facing compatibility issues.

### **WSL2-specific issues**

* Update WSL: `wsl --update` (from Windows)
* Ensure GPU passthrough is enabled
* Run `nvidia-smi` inside WSL to confirm access

---

## **FAQs**

**• Which CUDA version should I choose?**
Use the newest PyTorch CUDA build that is **≤ your driver’s max CUDA**. For most users, **CUDA 12.8** is ideal.

**• Do I need to install the system CUDA toolkit?**
No. PyTorch bundles its own CUDA runtime. Install system CUDA only if some *other* software requires it.

**• PyTorch sees my GPU but training is slow — what can I do?**

* Enable mixed precision (`torch.cuda.amp`)
* Use `pin_memory=True` in your DataLoader
* Increase batch size if VRAM allows
* Set:

```python
torch.set_float32_matmul_precision("high")
```

**• Does PyTorch support AMD GPUs?**
Yes, via **ROCm**. Use the ROCm build and confirm your GPU is on AMD’s ROCm compatibility list.

---

## **Need More Help?**

* **PyTorch Official Docs**: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
* **uv Documentation**: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
* **NVIDIA CUDA Docs**: [https://docs.nvidia.com/cuda/](https://docs.nvidia.com/cuda/)
* **GitHub Issues (PyTorch)**: [https://github.com/pytorch/pytorch/issues](https://github.com/pytorch/pytorch/issues)

---

*Last Updated: 02-12-2025*
*GitHub Author: @mchadolias*
