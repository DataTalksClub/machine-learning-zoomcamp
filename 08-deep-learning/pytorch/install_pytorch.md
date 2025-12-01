# **Complete PyTorch Installation Guide (GPU & CPU Support)**

Hi 👋  
This guide walks you through installing PyTorch with GPU acceleration. It covers multiple package managers (uv, pip, conda), explains CUDA compatibility, and includes verification and benchmarking scripts.

Tested on Linux and WSL2.

---

## **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [Step-by-Step Installation](#step-by-step-installation)
   - [Step 1: Check Your Graphics Card](#step-1-check-your-graphics-card)
   - [Step 2: Choose and Setup Package Manager](#step-2-choose-and-setup-package-manager)
   - [Step 3: Install PyTorch](#step-3-install-pytorch)
   - [Step 4: Verify Installation](#step-4-verify-installation)
3. [GPU vs CPU](#gpu-vs-cpu)
4. [Troubleshooting Common Issues](#troubleshooting-common-issues)
5. [Best Practices](#best-practices)
6. [FAQs](#faqs)

---

## **Prerequisites**

Before installing PyTorch, ensure your system meets these requirements:

### **System Requirements**

- **OS**: Linux, WSL2 (recommended for Windows), or macOS
- **Shell**: bash, zsh, or similar
- **Python**: 3.9 or later (always check beforehand)
- **Memory**: Minimum 8 GB RAM, 16+ GB recommended for deep learning

### **GPU-Specific Requirements**

- **NVIDIA GPU**: Compute capability ≥ 3.5 (most GPUs from 2014+)
- **NVIDIA Driver**: Latest version recommended
- **AMD GPU**: ROCm support (check compatibility)
- **Integrated Graphics**: CPU-only mode available but not recommended for training

### **Package Managers**

Choose one based on your needs:

- **uv** ⚡ (Recommended): Fast, modern, reliable
- **pip**: Universal, simple
- **conda**: Excellent dependency management
- **pipenv**: Good for application deployment

> **📝 Note for Seminar Participants**: This seminar recommends **uv** for its speed and reliability.

---

## **Step-by-Step Installation**

### **Step 1: Check Your Graphics Card**

The first step is to identify your GPU's compute capabilities. This determines whether you can use GPU acceleration and which CUDA version to choose.

**For NVIDIA GPUs:**

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

In this example:

- `Driver Version`: 580.105.08
- `CUDA Version` (max supported): 13.0
- `GPU Model`: NVIDIA GeForce GTX 1650

**Important Notes:**

1. The CUDA version shown is the maximum version your driver supports, not what you need to install
2. PyTorch bundles its own CUDA toolkit - you don't need to install CUDA separately
3. It's generally safe to use the latest CUDA version that PyTorch supports

**Key information to note:**

- **Driver Version**: Should be ≥ 525 for CUDA 12.x
- **CUDA Version**: Maximum CUDA version your driver supports
- **GPU Model**: Check compute capability

**Check compute capability:**

```bash
nvidia-smi --query-gpu=compute_cap --format=csv
```

You can check specific GPU capabilities on NVIDIA's [CUDA GPU list](https://developer.nvidia.com/cuda-gpus).

**For AMD GPUs:**

```bash
amd-smi
```

AMD uses its own framework called ROCm. Check compatibility at the AMD GPU [Architecture Table](https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html).

**For Intel/Integrated Graphics:**
You'll use CPU-only installation.

> **⚠️ Important**: The CUDA version in `nvidia-smi` is the **maximum supported**, not what you need to install. PyTorch bundles its own CUDA toolkit.

### **Step 2: Choose and Setup Package Manager**

#### **Option A: Using uv (Recommended)**

**Install uv:**

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Alternative: via pip
pip install uv

# Verify installation
uv --version
```

**Create virtual environment:**

```bash
# Create environment
uv venv pytorch-env

# Activate it
source pytorch-env/bin/activate  # Linux/macOS
# OR
.\pytorch-env\Scripts\activate   # Windows
```

#### **Option B: Using pip**

**Create virtual environment:**

```bash
python -m venv pytorch-env
source pytorch-env/bin/activate  # Linux/macOS
.\pytorch-env\Scripts\activate   # Windows
```

#### **Option C: Using conda**

**Install Miniconda/Anaconda, then:**

```bash
conda create -n pytorch-env python=3.10
conda activate pytorch-env
```

### **Step 3: Install PyTorch**

PyTorch provides different versions for different CUDA versions, AMD ROCm, and CPU-only setups. Currently supported versions include CUDA 12.6, 12.8, 13.0, and ROCm 6.4.

#### **CUDA Version Compatibility Guide**

| Your Driver Shows | Recommended PyTorch CUDA | Reason |
|------------------|--------------------------|--------|
| CUDA 11.x | CUDA 11.8 | Maximum compatibility |
| CUDA 12.0-12.5 | CUDA 12.1 | Stable, widely supported |
| CUDA 12.6+ | CUDA 12.8 | Latest stable |
| CUDA 13.0+ | CUDA 12.8 or 13.0 | 12.8 is more stable |
| No GPU/Other | CPU | For inference/small models |

#### **Installation Commands**

**Using uv:**

```bash
# For CUDA 12.8 (recommended for most users)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# For CUDA 12.6
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# For AMD ROCm 6.4
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.4

# For CPU-only
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

> **⚠️ Important** If you encounter Python version conflicts, you can always downgrade.

```bash
# Downgrade Python if needed
conda create -n pytorch-env python=3.10 pytorch torchvision torchaudio pytorch-cuda=12.8 -c pytorch -c nvidia
```

### **Step 4: Verify Installation**

Run this simple verification script to confirm PyTorch is installed correctly and can access your GPU:

**Basic Verification Script (`scripts/verify_basic.py`):**

---

## **GPU vs CPU**

GPUs are strongly recommended over CPUs for deep learning because they can perform thousands of calculations simultaneously, while CPUs process tasks sequentially. This parallel processing capability is perfect for the matrix operations that form the foundation of neural networks.

**Prove it to yourself:** Run the benchmark script below to see exactly how much faster your GPU performs compared to CPU!

**File: `scripts/benchmark_gpu_cpu.py`**

---

## **Troubleshooting Common Issues**

### **Issue 1: CUDA Not Available**

```bash
# Check if PyTorch sees CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Solution steps:
1. Update NVIDIA drivers: https://www.nvidia.com/Download/index.aspx
2. Verify GPU compute capability: nvidia-smi --query-gpu=compute_cap --format=csv
3. Reinstall PyTorch with correct CUDA version
4. For WSL2: Ensure GPU passthrough is enabled
```

### **Issue 2: Out of Memory (OOM)**

```python
# Reduce batch size
batch_size = 32  # Try 16, 8, or 4

# Use gradient accumulation
accumulation_steps = 4
loss.backward()
if (batch_idx + 1) % accumulation_steps == 0:
    optimizer.step()
    optimizer.zero_grad()

# Use mixed precision
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()

with autocast():
    output = model(input)
    loss = criterion(output, target)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

### **Issue 3: Python Version Conflicts**

```bash
# With uv: Specify Python version during env creation
uv venv --python 3.10 pytorch-env

# With conda: Specify Python in conda create
conda create -n pytorch-env python=3.10 pytorch torchvision torchaudio

# With pip: Use specific Python version
python3.10 -m venv pytorch-env
```

### **Issue 4: Slow Installation/Download**

```bash
# Use uv with --no-cache
uv pip install --no-cache torch torchvision torchaudio

# Use pip with timeout and retry
pip install --default-timeout=100 --retries 10 torch torchvision torchaudio
```

### **WSL2-Specific Issues**

```bash
# 1. Ensure WSL2 is updated
wsl --update

# 2. Install NVIDIA CUDA on WSL from Microsoft Store
# 3. Enable GPU passthrough in .wslconfig:
# [wsl2]
# gpuSupport=true

# 4. Verify in WSL
nvidia-smi
```

---

## **Best Practices**

### **Monitoring Tools**

```bash
# Real-time GPU monitoring
watch -n 1 nvidia-smi

# With process details
nvidia-smi --query-compute-apps=pid,process_name,used_memory,gpu_util --format=csv
```

---

## **FAQs**

### **Q: Which CUDA version should I choose?**

**A**: Use the **latest stable CUDA version** that PyTorch supports and that is ≤ your driver version. As of 2024, CUDA 12.8 is recommended for most users.

### **Q: Should I install system CUDA toolkit separately?**

**A**: **No need**. PyTorch bundles its own CUDA toolkit. Only install system CUDA if you need it for other applications.

### **Q: PyTorch detects GPU but training is slow?**

**A**:

1. Check if data transfer is bottleneck: `pin_memory=True` in DataLoader
2. Enable mixed precision: `torch.cuda.amp`
3. Increase batch size (if memory allows)
4. Set `torch.set_float32_matmul_precision('high')`

### **Q: AMD GPU support?**

**A**: Yes, via ROCm. Use the ROCm installation commands. Check [AMD ROCm compatibility](https://rocm.docs.amd.com) for your specific GPU.

---

## **Quick Reference Cheat Sheet**

```bash
# 1. Check GPU
nvidia-smi

# 2. Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Create environment
uv venv pytorch-env
source pytorch-env/bin/activate

# 4. Install PyTorch (CUDA 12.8)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# 5. Verify
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# 6. Run benchmark
python benchmark_gpu_cpu.py
```

---

## **Need More Help?**

- **PyTorch Official Docs**: https://pytorch.org/get-started/locally/
- **uv Documentation**: https://docs.astral.sh/uv/
- **NVIDIA CUDA Docs**: https://docs.nvidia.com/cuda/
- **Seminar Forum**: Check your course materials
- **GitHub Issues**: https://github.com/pytorch/pytorch/issues

---

*Last Updated: 01-12-2025*
*GitHub Author: @mchadolias*
