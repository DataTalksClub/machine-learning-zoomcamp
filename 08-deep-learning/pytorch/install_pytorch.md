# Installation guide for PyTorch

Hi 👋
This is a small guide to how you can install PyTorch to your PC, with or without GPU support. This might serve for the deep-learning part of the module, but for deep learning activities in general. This guide has been tested in a Linux-based subsystem, but in principle should work in WSL as well.

## Prerequisites

- Linux OS or WSL
- bash/zsh shell
- Python
- Package manager (`pip`)
- Python manager (`uv`, `conda`, `pipenv`, etc)

## prerequisites

- Linux OS or WSL
- bash/zsh shell
- Python
- Package manager (`pip`)
- Python manager (`uv`, `conda`, `pipenv`, etc)

## Step Guide

### Step 1: Check your Graphics Card

The first part is to identify the compute capabilities of the GPU that your system is using.

For systems that are using an NVIDIA GPU, using the `nvidia-smi` command lets the user find out valuable information regarding the Graphics Cards and its software. For us, it's useful to check the CUDA version that your system is using and the model name of the card.

```bash
nvidia-smi
```

Example output (shortened):

```
Sat Nov 29 19:40:41 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
|   0  NVIDIA GeForce GTX 1650        Off |   00000000:01:00.0  On |                  N/A |
| N/A   47C    P8              2W /   50W |    1173MiB /   4096MiB |     16%      Default |
+-----------------------------------------+------------------------+----------------------+
```

For my case as listed above it is `CUDA Version: 13.0` and `Model name: NVIDIA GeForce GTX 1650`

**Important**: The CUDA version shown in `nvidia-smi` is the maximum version your driver supports, but PyTorch will use its own CUDA toolkit. It's generally safe to use the latest CUDA version that PyTorch supports.

Copy the name of your graphics card to find out its capabilities. For PyTorch to be effective with a graphics card, it needs to have a compute capability of 3.5 or higher. Most modern GPUs (2014+) meet this requirement. The GTX 1650 you listed has compute capability 7.5, which is excellent.

This can be easily checked from lookup tables. For instance, NVIDIA provides this one for its [models](https://developer.nvidia.com/cuda-gpus).

**Alternative method to check compute capability:**

```bash
nvidia-smi --query-gpu=compute_cap --format=csv
```

Similarly, for AMD Graphics cards the `amd-smi` command exists, with the following [table](https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html). It also uses its own framework called `ROCm`.

### Step 2: Visit the PyTorch docs

After the user has identified the system, it is time to visit the PyTorch documentation guide, where the exact capabilities of the system can be filled for the appropriate version of the framework to be provided. Here the user can decide to run deep learning only on its CPU for various reasons. However, generally it is not recommended for larger models.

**Note:** Remember to install the library inside your python environment to avoid conflicts with your system Python.

```bash
conda activate deep-learning-env # Or something similar for other managers
```

**Package Manager Note**: While `pip` works well, Conda often handles CUDA dependencies better and is recommended for easier dependency management.

As well as, PyTorch is provided apart from Python, also as a library for C++/Java called `libtorch`, though I haven't used it in that capacity so I can't provide any comment.

Currently, PyTorch is provided for CUDA 12.6, 12.8 and 13.0, as well as a separate AMD version, and the CPU-only option. Here are the following links for each option:

**CUDA 12.6 system:**

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

**CUDA 12.8 system:**

```bash
pip3 install torch torchvision
```

**CUDA 13.0 system:**

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

**AMD (ROCm 6.4) system:**

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/rocm6.4
```

**CPU-only option (Not recommended for training):**

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Verify that Pytoch is working with GPU

A simple script can be used as a test, to verify the proper installation of PyToch to your system. I have provided the one that I used personally when working for the module. 

```python
import torch
import sys

print("=" * 50)
print("Framework GPU Verification")
print("=" * 50)

# System and Python info
print(f"Python version: {sys.version}")
print()

# PyTorch Info
print("\nPYTORCH:")
print(f"  Version: {torch.__version__}")
print(f"  CUDA Available: {torch.cuda.is_available()}")
print(f"  CUDA Version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"  GPU Device: {torch.cuda.get_device_name(0)}")
    print(f"  GPU Count: {torch.cuda.device_count()}")

    # Test PyTorch GPU computation
    device = torch.device("cuda")
    x = torch.randn(3, 3).to(device)
    y = torch.randn(3, 3).to(device)
    z = x + y
    print(f"  GPU Test: Computation successful on {z.device}")
else:
    print("  GPU Test: Using CPU")
```

The output should be something similar to that

```bash
==================================================
Framework GPU Verification
==================================================
Python version: 3.13.7 | packaged by conda-forge | (main, Sep  3 2025, 14:30:35) [GCC 14.3.0]

PYTORCH:
  Version: 2.9.1+cu126
  CUDA Available: True
  CUDA Version: 12.6
  GPU Device: NVIDIA GeForce GTX 1650
  GPU Count: 1
  GPU Test: Computation successful on cuda:0
  Performance Test: 29.89 ms
==================================================
```

## Why Use GPU for Deep Learning?

GPUs are strongly recommended over CPUs for deep learning because they can perform thousands of calculations simultaneously, while CPUs process tasks sequentially. This parallel processing capability is perfect for the matrix operations that form the foundation of neural networks. In practice, this means:

- **Faster training**: Models that take days on CPU might take only hours on GPU
- **Practical workflows**: Makes experimenting with different models feasible
- **Better for larger models**: Handles complex architectures that would be too slow on CPU

The performance difference is substantial - typically 10x to 50x speed improvements for common deep learning tasks.

**Prove it to yourself**: Run the verification script in this guide to see exactly how much faster your GPU performs compared to CPU!

```python
import torch
import sys
import time

print("=" * 60)
print("PyTorch GPU Verification & Performance Benchmark")
print("=" * 60)

# System and Python info
print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")
print()

# PyTorch Info
print("SYSTEM INFORMATION:")
print(f"  CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  CUDA Version: {torch.version.cuda}")
    print(f"  GPU Device: {torch.cuda.get_device_name(0)}")
    print(f"  GPU Count: {torch.cuda.device_count()}")
    print(
        f"  GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB"
    )
    print(f"  Compute Capability: {torch.cuda.get_device_capability()}")
else:
    print("  No GPU detected - using CPU only")

print("\n" + "=" * 60)
print("PERFORMANCE BENCHMARK")
print("=" * 60)


def benchmark_operation(operation_name, operation, device, size=1000, iterations=100):
    """Benchmark a single operation on specified device"""
    # Warm-up
    for _ in range(10):
        _ = operation(device, size)

    # Benchmark
    start_time = time.time()
    for _ in range(iterations):
        result = operation(device, size)
    end_time = time.time()

    # Sync if CUDA
    if device.type == "cuda":
        torch.cuda.synchronize()

    return (end_time - start_time) * 1000  # Convert to milliseconds


# Define benchmark operations
def matmul_operation(device, size=1000):
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    return torch.matmul(a, b)


def elementwise_operation(device, size=1000):
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    return a * b + torch.sin(a) - torch.cos(b)


def convolution_operation(device, size=1000):
    # Smaller size for conv to avoid memory issues
    channels = 32
    spatial = min(size // 8, 128)
    x = torch.randn(1, channels, spatial, spatial, device=device)
    conv = torch.nn.Conv2d(channels, channels, 3, padding=1, device=device)
    return conv(x)


# Available devices
devices = [torch.device("cpu")]
if torch.cuda.is_available():
    devices.append(torch.device("cuda"))

# Run benchmarks
operations = [
    ("Matrix Multiplication (1000x1000)", matmul_operation),
    ("Element-wise Operations", elementwise_operation),
    ("Convolution Operation", convolution_operation),
]

results = {}

for op_name, op_func in operations:
    print(f"\n{op_name}:")
    results[op_name] = {}

    for device in devices:
        try:
            time_taken = benchmark_operation(op_name, op_func, device)
            results[op_name][device.type] = time_taken
            print(f"  {device.type.upper():<6}: {time_taken:8.2f} ms")
        except RuntimeError as e:
            print(f"  {device.type.upper():<6}: Failed - {str(e)}")
            results[op_name][device.type] = None

# Calculate speedup
print("\n" + "=" * 60)
print("PERFORMANCE SUMMARY")
print("=" * 60)

if torch.cuda.is_available():
    for op_name in results:
        cpu_time = results[op_name].get("cpu")
        cuda_time = results[op_name].get("cuda")

        if cpu_time and cuda_time and cuda_time > 0:
            speedup = cpu_time / cuda_time
            print(f"{op_name}:")
            print(f"  Speedup: {speedup:6.1f}x faster on GPU")
            if speedup > 1:
                print(f"  GPU is {speedup:.1f}x faster than CPU")
            else:
                print(f"  CPU is {1/speedup:.1f}x faster than GPU")
        else:
            print(f"{op_name}: Comparison not available")

    # Memory benchmark
    print(f"\nMEMORY BENCHMARK:")
    try:
        # Test large tensor allocation
        large_tensor_gpu = torch.randn(5000, 5000, device=torch.device("cuda"))
        gpu_memory_usage = (
            large_tensor_gpu.element_size() * large_tensor_gpu.nelement() / 1024**2
        )
        print(f"  Allocated {gpu_memory_usage:.1f} MB on GPU successfully")
        del large_tensor_gpu
        torch.cuda.empty_cache()
    except RuntimeError as e:
        print(f"  GPU memory test failed: {e}")

# Final verification
print("\n" + "=" * 60)
print("FINAL VERIFICATION")
print("=" * 60)

if torch.cuda.is_available():
    # Test basic GPU functionality
    device = torch.device("cuda")

    # Simple computation test
    x = torch.randn(100, 100, device=device)
    y = torch.randn(100, 100, device=device)
    z = x + y

    # Backward pass test
    w = torch.randn(10, 10, device=device, requires_grad=True)
    loss = w.sum()
    loss.backward()

    print("✓ Basic GPU computation: SUCCESS")
    print("✓ GPU gradient computation: SUCCESS")
    print(f"✓ Final tensor device: {z.device}")

    # Memory info
    allocated = torch.cuda.memory_allocated() / 1024**2
    cached = torch.cuda.memory_reserved() / 1024**2
    print(f"✓ GPU memory allocated: {allocated:.1f} MB")
    print(f"✓ GPU memory cached: {cached:.1f} MB")

    print("\n🎉 PyTorch GPU setup is working correctly!")
else:
    print("⚠️  Running in CPU-only mode")
    print("💡 For GPU acceleration, check your CUDA installation and drivers")

print("=" * 60)
```

After running the script for my systeml, I got the following results 🎉


```bash
============================================================
PyTorch GPU Verification & Performance Benchmark
============================================================
Python version: 3.13.7 | packaged by conda-forge | (main, Sep  3 2025, 14:30:35) [GCC 14.3.0]
PyTorch version: 2.9.1+cu126

SYSTEM INFORMATION:
  CUDA Available: True
  CUDA Version: 12.6
  GPU Device: NVIDIA GeForce GTX 1650
  GPU Count: 1
  GPU Memory: 3.6 GB
  Compute Capability: (7, 5)

============================================================
PERFORMANCE BENCHMARK
============================================================

Matrix Multiplication (1000x1000):
  CPU   :  1621.47 ms
  CUDA  :     3.31 ms

Element-wise Operations:
  CPU   :  1190.33 ms
  CUDA  :     5.02 ms

Convolution Operation:
  CPU   :   360.74 ms
  CUDA  :    14.21 ms

============================================================
PERFORMANCE SUMMARY
============================================================
Matrix Multiplication (1000x1000):
  Speedup:  490.1x faster on GPU
  GPU is 490.1x faster than CPU
Element-wise Operations:
  Speedup:  237.2x faster on GPU
  GPU is 237.2x faster than CPU
Convolution Operation:
  Speedup:   25.4x faster on GPU
  GPU is 25.4x faster than CPU

MEMORY BENCHMARK:
  Allocated 95.4 MB on GPU successfully

============================================================
FINAL VERIFICATION
============================================================
✓ Basic GPU computation: SUCCESS
✓ GPU gradient computation: SUCCESS
✓ Final tensor device: cuda:0
✓ GPU memory allocated: 8.7 MB
✓ GPU memory cached: 22.0 MB

🎉 PyTorch GPU setup is working correctly!
============================================================
```

## Additional Recommendations

### Troubleshooting Common Issues

**If CUDA is not available:**

1. Check your NVIDIA driver version: `nvidia-smi`
2. Verify PyTorch CUDA version matches your system capability
3. Try reinstalling with the correct CUDA version

**For WSL Users:**

- Ensure you have WSL 2 with GPU passthrough enabled
- Install NVIDIA CUDA on WSL from the Microsoft Store

### Performance Tips

- Use `torch.set_float32_matmul_precision('high')` for better performance on modern GPUs
- Consider using mixed precision training with `torch.cuda.amp` for larger models
- Monitor GPU usage with `watch -n 1 nvidia-smi` during training

### Virtual Environment Best Practices

```bash
# Using conda (recommended)
conda create -n pytorch-env python=3.10
conda activate pytorch-env

# Using venv
python -m venv pytorch-env
source pytorch-env/bin/activate
```
