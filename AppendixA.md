## Appendix A: Setting Up Your GPU Pod

You don’t need to spend hundreds or even thousands of dollars on a high-end GPU to fine-tune your LLMs quickly. There are plenty of providers out there, with **Google Colab** being one of the most popular. Google Colab offers a GPU-enabled _free tier_ (Tesla T4 with 15 GB RAM), which is more than sufficient for many tasks. However, that GPU **doesn’t support the fancy BF16 data type or Flash Attention 2**. Plus, training even a medium-sized language model on it will require a lot of patience.

If you want to speed things up, you'll have to spend a little money. Particularly, I like to use [runpod.io](https://runpod.io) to rent an RTX 4090 with 24GB RAM (this is not sponsored by them and it's not affiliate marketing either; I'm just a happy customer). A few months ago, when I started writing this book, it used to cost $0.44 per hour (in the community cloud). Now, it's down to $0.34 per hour. So, even if you spend the whole business day training models non-stop, it will cost you less than three dollars. It's great for small projects.

***
**DISCLAIMER**: The information provided here is for educational purposes only. While every effort has been made to ensure accuracy and completeness, it's ultimately the reader's responsibility to understand their own specific needs and circumstances when selecting and utilizing cloud services. By using or relying on any cloud service discussed in this book, you acknowledge that: (a) you have read and understood the terms and conditions of each service provider, including any applicable fees and charges; (b) you are aware of the potential for costs to arise due to your failure to properly terminate or downsize cloud services as needed; and (c) the author and publisher of this book disclaim any responsibility or liability for any financial loss, damage, or other consequences resulting from your use of cloud services. Please note that it's essential to carefully review and understand the pricing structures, terms, and conditions of each service provider before making a decision. It's also crucial to regularly monitor and manage your cloud usage to avoid unexpected costs.
***

In this appendix, I’ll walk you through the steps to set up your own GPU-backed pod running Jupyter Notebook. I’m assuming you’ve already signed up for an account and are viewing the dashboard. If you click on "Pods" in the menu, you should see something like this:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod1.png?raw=True)

Click on the big purple "Deploy" button and it will take to you the "Deploy GPU Pod" screen:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod2.png?raw=True)

Choose "GPU" and, for experimenting with your own projects, the "Community Cloud," which is cheaper. You may also choose the country where your pod will be based. In my experience, the deployment is usually faster when I choose the United States. The availability of GPUs may change depending on the chosen country, day of the week, and time of day. There are times when good and affordable GPUs (like an RTX 4090) are not available.

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod3.png?raw=True)

Once you've clicked on the GPU of your choice, it will automatically scroll down to select the pod template. Click on the "Change Template" button to the right and search for "jupyter":

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod3_1.png?raw=True)

Select "Jupyter PyTorch" and you'll go back to the previous screen. At this point, you get to choose how many GPUs you want and if you'd like to use an "On-Demand" or "Spot" instance. Spot instances are cheaper but may be terminated abruptly. Next, click the long purple "Deploy" button at the bottom:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod4.png?raw=True)

Now, your pod is being deployed. It will download a Docker image and spin it up. The whole process may take a few minutes (if it's annoyingly slow, consider starting over and perhaps choosing a different country). If you click on the arrow to the right, you'll see what's happening:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod5.png?raw=True)

Once it's finished deploying your pod, your dashboard should look like this:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod6.png?raw=True)

There's plenty of information you can come back to at any point, like CPU and GPU utilization and memory usage. Click on the purple "Connect" button, and you'll be taken to the following screen:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod7.png?raw=True)

Sometimes, one or more of the "Connect to..." buttons at the top may not be ready yet (they will show up in red). It may take a minute or two, but once they become purple, you can click on them. Click on the third one to connect to Jupyter's port (8888), and you'll see the login screen below:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod8.png?raw=True)

The correct way to enter your login credentials is to use "_user_" as the username and "_password_" as the password. This will grant you access to a list of running services:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod9.png?raw=True)

In the bottom-right corner, click on "Direct/Default" corresponding to the "Jupyter Notebook" service—and you'll have a GPU-powered Jupyter Notebook at your disposal!

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod10.png?raw=True)

You can choose to start a notebook from scratch or upload one of your own choice (for example, `Chapter0.ipynb`).

Now, would you like to use Flash Attention 2 in your notebook? If so, you can upload the `FA2 Install.ipynb` notebook from the official GitHub repository for this book and run it to download and install all requirements.

### Stopping And Terminating Your Pod

Once you're done, **don't forget to stop and terminate your pods**. Go back to the list of your pods and click on the "Stop" button (the second button in the bottom-left corner):

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod11.png?raw=True)

At this point, you'll receive a message asking you to confirm and warning you that **you're not done yet—terminating your pod is still necessary**. Click on "Stop Pod".

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod12.png?raw=True)

The pod is stopped but has not yet been terminated, so it is still listed on your list of pods. Click on the arrow on the right to expand its information:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod13.png?raw=True)

To **truly terminate your pod**, you need to click on the purple "Trash" button:

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod14.png?raw=True)

It will ask you for a final confirmation.

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/runpod15.png?raw=True)

Click the "Yes" button to confirm that you want to terminate your pod. Your pod will be shut down at this point.

### Flash Attention 2 Install

This short installation guide is divided into two parts: CUDA Toolkit and Pip Install. The first part covers installation instructions for the NVIDIA CUDA Compiler (NVCC) driver, which is a requirement for installing the Flash Attention 2 library covered in the second part.

If you're using the "Jupyter PyTorch" template from runpod.io and you try running the command below, it will inform you that it couldn't find the command:

```
!nvcc --version
```

```
/bin/bash: line 1: nvcc: command not found
```

If, however, you're running this in a different environment, and you get an output like the one below, it means you already have NVCC installed:

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Thu_Sep_12_02:18:05_PDT_2024
Cuda compilation tools, release 12.6, V12.6.77
Build cuda_12.6.r12.6/compiler.34841621_0
```

If that's the case, please skip directly to the "pip install" section.

#### CUDA Toolkit Install

The "Jupyter PyTorch" template is based on a Docker image that uses Ubuntu. First, we need to determine which Ubuntu version is running:

```
!lsb_release -a
```

```
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.4 LTS
Release:	22.04
Codename:	jammy
```

That's Ubuntu 22.04, great. We can now head to NVIDIA's [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) page and select the proper configuration:

* **Operating System**: `Linux`
* **Architecture**: `x86_64`
* **Distribution**: `Ubuntu`
* **Version**: `22.04`
* **Install Type**: `deb(local)`

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/cuda1.png?raw=True)

Once you've finished selecting the configuration, it will show you a list of installation instructions.

![](https://github.com/dvgodoy/FineTuningLLMs/blob/main/images/appendixA/cuda2.png?raw=True)

We're dividing these instructions into four groups:

- **Group 1: Downloading Only**: this group is easy, fast, and straightforward. Just run the commands below, then wait a few seconds for it to finish running:
  - `!wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin`
  - `!sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600`
- **Group 2: Downloading and Installing**: the versions used in the commands below (12.6.2 and 12.6.2-560.35.03-1) may change between the time of writing and your visit to NVIDIA's page. It should work fine if you run the commands below "as is" but, if you want to get the latest version, make sure to copy them from the configuration page and update accordingly. These commands will take a few minutes to run:
  - `!wget https://developer.download.nvidia.com/compute/cuda/12.6.2/local_installers/cuda-repo-ubuntu2204-12-6-local_12.6.2-560.35.03-1_amd64.deb`
  - `!sudo dpkg -i cuda-repo-ubuntu2204-12-6-local_12.6.2-560.35.03-1_amd64.deb`
  - Once it finishes running, it will print out the command you need to run in the next step:
    - `sudo cp /var/cuda-repo-ubuntu2204-12-6-local/cuda-F9A63CE3-keyring.gpg /usr/share/keyrings/`
- **Group 3: Editing the Command**: the only command in this group must be exactly the one listed in the last line of the output from Group 2. It will run instantly since it's only copying a file to a different directory:
  - `!sudo cp /var/cuda-repo-ubuntu2204-12-6-local/cuda-XXXXXXXX-keyring.gpg /usr/share/keyrings/`
- **Group 4: Installing Only**: we're now ready to install the CUDA Toolkit itself. I've added `--fix-missing` to the last command to make it more robust. These two commands will take quite a while to run:
  - `!sudo apt-get update`
  - `!sudo apt-get -y install cuda-toolkit-12-6 --fix-missing`

#### Checking the Installation

After installing everything, you should be able to successfully run the command listed below:

```
!nvcc --version
```

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Thu_Sep_12_02:18:05_PDT_2024
Cuda compilation tools, release 12.6, V12.6.77
Build cuda_12.6.r12.6/compiler.34841621_0
```

### Pip Install

If you already have the NVIDIA CUDA compiler driver installed, installing Flash Attention 2 itself is a piece of cake:

```
!pip install -U flash-attn transformers
```

Once it's finished installing, you can run Transformers' helper function, `is_flash_attn_2_available()`:

```python
from transformers.utils import is_flash_attn_2_available
is_flash_attn_2_available()
```

```
True
```

That's it! Enjoy Flash Attention 2!