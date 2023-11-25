# Installation of tensorflow

date: 2023 Nov 12

This installation guide is specific to the use case as in the pre-requisites. I'm not sure if it is similar for Mac/Linux native OSes or Other WSL2 Distros. Let me know either way if it does help.

Also, welcome to edit and make corrections directly (via PRs) or let me know via Slack.


## pre-requisites
- wsl2 on Windows 10 19044 or higher
- Nvidia Pascal GPU, current driver 546.01
- Ubuntu 22.04 LTS
- micromamba environment manager
- bash/zsh shell
- cuda_12.3.0_545.84_windows.exe and cudnn-windows-x86_64-8.9.6.50_cuda12-archive.zip 
- Nvidia CUDA Toolkit 12.3 on WSL2
- Tensorflow v2.14 with cuda


## starting over or pre-install

### windows host

1. control panel --> Uninstall Cuda v??.?
2. verify Nvidia driver is >= v450.xx (currently v546.01 as of @2023 Nov 12)
3. [download cuda executable for Win10](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
   - install following screen prompts, but select `Custom Install`, shorten the Path if desired. I've shorten from the defaults to just `cuda`
   - disable nsight, visual studio, GPU driver, GeForce Experience, HD Audio driver (if installed separately)
   - add to PATH manually or verify these are present; first 2 are mandatory, 3rd might be optional (I'm not sure):
     - `C:\Program Files\cuda\v12.3\bin`
     - `C:\Program Files\cuda\v12.3\libnvvp`
     - `D:\Program Files\cuda\v12.3\extras\CUPTI\lib64`
4. [cudnn-windows-x86_64-8.9.6.zip](https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.6/local_installers/12.x/cudnn-windows-x86_64-8.9.6.50_cuda12-archive.zip/), [download cudnn archive for other versions](https://developer.nvidia.com/rdp/cudnn-archive)
   - unzip and drag contents into the `C:\Program Files\cuda\v12.3\` where the matching `bin`, `include` and `lib` are located. Let the contents from `cudnn*.zip` replace the folders in the `CUDA` folder

### wsl2 Ubuntu 22.04

[source](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#removing-cuda-toolkit-and-driver) --> go to Ubuntu and Debian section

In the wsl2 Ubuntu terminal, clean up previous installs especially if on a different version
```bash
sudo apt-key del 7fa2af80
sudo apt-get --purge remove "*cuda*" "*cublas*" "*cufft*" "*cufile*" "*curand*" \
 "*cusolver*" "*cusparse*" "*gds-tools*" "*npp*" "*nvjpeg*" "nsight*" "*nvvm*"
sudo apt-get --purge remove "*nvidia*" "libxnvctrl*"
sudo apt-get autoremove
rm -rf "*.deb" "*.tar" "*.gz"
```

[source: go here for exact version numbers, other than 12.3 @2023 Nov 12](https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/)
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.3.0/local_installers/cuda-repo-wsl-ubuntu-12-3-local_12.3.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-12-3-local_12.3.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-12-3-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-3
```


## post Install

```bash
export PATH=/usr/local/cuda-12.3/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.3/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```


## create new environment

```bash
micromamba create -n py310 python=3.10
```

## activate environment

```bash
micromamba activate py310
```

## install tensorflow

```bash
pip install 'tensorflow[and-cuda]'
or
python3 -m pip install 'tensorflow[and-cuda]'
```

Outcome:

in virtual environment
- tensorflow-2.14
- tensorboard<2.15,>=2.14
- keras<2.15,>=2.14.0

in wsl2
- nvidia-cuda-runtime-cu12==11.8.89
- nvidia-cudnn-cu12==8.7.0.84
- 



## verify install

1. Run test_tf.ipynb to check if GPU recognized, or
2. Run the notebook.ipynb cells, and use `nvidia-smi` while it's running. Ensure the correct versions are reported in `nvidia-smi` output.

   - Driver version
   - CUDA version
   - processes list your python version
   - if you repeatedly run it with the up-arrow key<ENTER> you should be able to see the values of FAN%, Temp, Wattage, Memory, and Util change each time


```bash
nvidia-smi                                            
Sun Nov 12 22:59:54 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 545.29.01              Driver Version: 546.01       CUDA Version: 12.3     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce GTX 970         On  | 00000000:01:00.0  On |                  N/A |
| 40%   61C    P2              93W / 200W |   3872MiB /  4096MiB |     54%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A        23      G   /Xwayland                                 N/A      |
|    0   N/A  N/A      2490      C   /python3.10                               N/A      |
+---------------------------------------------------------------------------------------+
```

## FAQs

> **Issue**: `/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link`
> 
> **Solution**: paste this `ldconfig = false` entry into `[automount]` section in your `%USERPROFILE%/.wslconfig` file. Open the file in `vs-code` or text editor like `notepad++`. Mine's at `"C:\Users\Ella\.wslconfig"`. I had a previous entry to cap my RAM usage in WSL2.
> [source](https://github.com/microsoft/WSL/issues/5548#issuecomment-724674428)

```bash
[wsl2] 
memory=12GB

[automount]
ldconfig = false
```

|=============================================================================|

> **Issue**: warnings and info messages
> 
> **Solution**: surpress with 
> [source](https://stackoverflow.com/questions/35911252/disable-tensorflow-debugging-information)

```python
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
```

|=============================================================================|
