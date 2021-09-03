##  Setting up the Environment

In this section, we'll prepare the environment

## Anaconda

The easiest way to set up the environment is to use [Anaconda](https://www.anaconda.com/products/individual)

### Linux

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
bash Anaconda3-2021.05-Linux-x86_64.sh
```

### Windows

* Use WSL and follow the instructions for Lunux
* Or use the graphical installer [from here](https://www.anaconda.com/products/individual)


## Miniconda 

Miniconda is a smaller version of Anaconda that contains only Python. It doesn't have all the data science


You can see how to install it [here](https://docs.conda.io/en/latest/miniconda.html).


For Linux (for Python 3.8 version):

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh
bash Miniconda3-py38_4.10.3-Linux-x86_64.sh
```


## Installing the libraries with pip

```bash
pip install numpy pandas scikit-learn seaborn jupyter
```

You don't need to do it if you use Anaconda (it already contains all these libraries).

But Anaconda doesn't have XGBoost and TensorFlow, so you'll need to install them:

```bash
pip install xgboost 
pip install tensorflow
```


## AWS 

You can rent an instance on AWS:

* [Creating an AWS account](https://mlbookcamp.com/article/aws)
* [Renting an ec2 instance](https://mlbookcamp.com/article/aws-ec2)



## Navigation

* [Machine Learning Zoomcamp course](../)
* [Lesson 1: Introduction to Machine Learning](README.md)
* Previous lesson: [The Modelling Step (Model Selection Process)](05-model-selection.md)
* Next lesson: [Introduction to NumPy](07-numpy.md)