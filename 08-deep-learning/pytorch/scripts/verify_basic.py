import torch
import torchvision

print("=" * 50)
print("PyTorch Installation Verification")
print("=" * 50)

print(f"PyTorch version: {torch.__version__}")
print(f"Torchvision version: {torchvision.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"\nGPU Information:")
    print(f"  Device: {torch.cuda.get_device_name(0)}")
    print(f"  CUDA version: {torch.version.cuda}")
    print(f"  GPU Count: {torch.cuda.device_count()}")
    memory_gb = torch.cuda.get_device_properties(0).total_memory / 1024**3
    print(f"  Memory: {memory_gb:.1f} GB")
    print(f"  Compute Capability: {torch.cuda.get_device_capability()}")
else:
    print("\nRunning in CPU-only mode")

print("=" * 50)
