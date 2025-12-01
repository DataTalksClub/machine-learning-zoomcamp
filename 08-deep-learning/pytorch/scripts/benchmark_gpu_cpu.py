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
                print(f"  CPU is {1 / speedup:.1f}x faster than GPU")
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
