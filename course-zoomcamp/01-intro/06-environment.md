##  Setting up the Environment

In this section, we'll prepare the environment

## Conda

The easiest way to set up the environment is to use [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Anaconda comes with the most commonly used libraries preinstalled in the `base` environment, Miniconda is a smaller version of Anaconda that contains only Python. 

It is a good idea to set up a dedicated environment for the course (and do not use this environment for other projects)

### 1. Download and install correct binary for your system

Follow the instructions on page for installing the correct package for your system (the site will automatically detect your operating system and suggest the correct package)

Anaconda : https://www.anaconda.com/products/individual

Miniconda: https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links

(If you are using Windows, you can use WSL instead and follow the installation instructions for linux)


### 2. Create environment for course:
In your terminal, run this command

```bash
conda create -n ml-zoomcamp python=3.8
```

### 3. Activate the enviroment
Do this whenever you are adding new packages for the course or working on coursework

```bash
conda activate ml-zoomcamp
```

### 4. Install libraries

Installing libraries available on conda

```bash
conda install numpy pandas scikit-learn seaborn jupyter
```

Optionally, if you want to use tensorflow locally with a GPU:

```bash
conda config --add channels conda-forge
conda install cudatoolkit=11.2
```

Additional libraries only available on pypi:

```bash
pip install xgboost 
pip install tensorflow
```

## Cloud

Instead of running things locally, you can use online services or rent a server 

### AWS 

You can rent an instance on AWS:

* [Creating an AWS account](https://mlbookcamp.com/article/aws)
* [Renting an ec2 instance](https://mlbookcamp.com/article/aws-ec2)

### Google Colab

TODO (PRs are welcome)

### Kaggle

To use Kaggle to open and run the Jupyter notebooks provided as part of this course do the following:
* Find the URL of the notebook hosted in github. [See this example](https://drive.google.com/file/d/1xavL-rglUoa-npsC9z3PAEMlQGgo_o27/view)
* In your web browser launch it as shown in below example

  https://kaggle.com/kernels/welcome?src=https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb



## Navigation

* [Machine Learning Zoomcamp course](../)
* [Lesson 1: Introduction to Machine Learning](README.md)
* Previous lesson: [The Modelling Step (Model Selection Process)](05-model-selection.md)
* Next lesson: [Introduction to NumPy](07-numpy.md)
