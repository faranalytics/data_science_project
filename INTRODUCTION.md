# The Data Science Project
A Python [flat-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) project template for data science projects.

## Introduction

In the data science domain projects are sometimes shared as an informal assemblage of scripts. A `requirements.txt` file is sometimes used in order to reconstruct the project's environment. Some solutions involve making changes to `sys.path` or setting the `PYTHONPATH` environment variable in order to facilitate imports.

This repository describes an alternative approach using a conventional Python [flat-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) project. It follows formal conventions for packaging a Python project. You install it into your environment just like an ordinary Python package. It consists of a single package with an [IMRaD](https://en.wikipedia.org/wiki/IMRAD)-like layout; it contains materials, methods, and results sub-packages. Project dependencies are specified in the `pyproject.toml` file.

One important advantage of this approach is that utility functions can be conveniently imported into notebooks from anywhere in the package. It makes imports seamless without having to modify `sys.path` or setting the `PYTHONPATH` environment variable.

## Table of Contents
- [Explore](#explore)
- [Create a Data Science Project Using the Cookiecutter](#create-a-data-science-project-using-the-cookiecutter)
- [Dependencies](#dependencies)
- [Pipelines](#pipelines)
- [Publish](#publish)

## Explore

You can clone this repository, explore, and modify it to meet your needs or [create a project using the cookiecutter](#create-a-data-science-project-using-the-cookiecutter).
### Clone the repository.
```bash
git clone https://github.com/faranalytics/data_science_project.git
```

### Change directory into the repository's project directory.
This is the top-level directory of a conventional Python package.
```bash
cd data_science_project/project
```

### The directory structure looks like this.
```
├── project ⬅ This is the project directory.  Optionally chose a name for your project.
    ├── __about__.py
    ├── LICENSE
    ├── package ⬅ This is the package directory.  Optionally give the package a unique name.
    │   ├── __init__.py
    |   ├── __main__.py
    │   ├── materials ⬅ You can put your datasets and models in the materials directory.
    │   │   ├── __init__.py
    │   │   └── README.md
    │   ├── methods ⬅ You can put your utility functions and notebooks in the methods directory.
    │   │   ├── __init__.py
    │   │   ├── notebooks
    │   │   │   └── main.ipynb
    │   │   ├── README.md
    │   │   └── utils.py
    │   └── results ⬅ You can put the outputs of your scripts (e.g., tables and visualizations) in the results directory.
    │       ├── __init__.py
    │       └── README.md
    ├── pyproject.toml
    └── README.md
```

### Activate your environment if you are using a package manager (e.g., conda).
```bash
conda activate <your-environment>
```

### Install the package in editable mode.  
An editable install, also known as a development install, will make changes to your package modules immediately available when you restart your kernel.
```bash
pip install -e .
```

## Examples
Open the `package/methods/notebooks/main.ipynb` notebook and run the cells.
```python
# Import the path of each sub-module.
from package.materials import MATERIALS_PATH
from package.methods import METHODS_PATH
from package.results import RESULTS_PATH
```
```python
# Import a utility function from the methods package.
from package.methods.utils import say_hello

say_hello()
```
```python
from pprint import pprint
import pickle

# Read data from the MATERIALS_PATH.
data = [
    line.strip().split(",")
    for line in open(MATERIALS_PATH.joinpath("iris/iris.data")).readlines()[:-1]
]

pprint(data)

# Write the data to the RESULTS_PATH.
pickle.dump(data, open(RESULTS_PATH.joinpath("data.pkl"), "wb"))
```
```bash
[['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'],
 ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'],
 ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa'],
 ['4.6', '3.1', '1.5', '0.2', 'Iris-setosa'],
 ['5.0', '3.6', '1.4', '0.2', 'Iris-setosa'],
 ['5.4', '3.9', '1.7', '0.4', 'Iris-setosa'],
 ['4.6', '3.4', '1.4', '0.3', 'Iris-setosa'],
 ['5.0', '3.4', '1.5', '0.2', 'Iris-setosa'],
 ['4.4', '2.9', '1.4', '0.2', 'Iris-setosa'],
 ['4.9', '3.1', '1.5', '0.1', 'Iris-setosa'],
 ['5.4', '3.7', '1.5', '0.2', 'Iris-setosa'],
 ['4.8', '3.4', '1.6', '0.2', 'Iris-setosa'],
 ['4.8', '3.0', '1.4', '0.1', 'Iris-setosa'],
 ['4.3', '3.0', '1.1', '0.1', 'Iris-setosa'],
 ['5.8', '4.0', '1.2', '0.2', 'Iris-setosa'],
 ['5.7', '4.4', '1.5', '0.4', 'Iris-setosa'],
 ['5.4', '3.9', '1.3', '0.4', 'Iris-setosa'],
 ['5.1', '3.5', '1.4', '0.3', 'Iris-setosa'],
 ['5.7', '3.8', '1.7', '0.3', 'Iris-setosa'],
 ['5.1', '3.8', '1.5', '0.3', 'Iris-setosa'],
 ['5.4', '3.4', '1.7', '0.2', 'Iris-setosa'],
 ['5.1', '3.7', '1.5', '0.4', 'Iris-setosa'],
 ['4.6', '3.6', '1.0', '0.2', 'Iris-setosa'],
 ['5.1', '3.3', '1.7', '0.5', 'Iris-setosa'],
 ['4.8', '3.4', '1.9', '0.2', 'Iris-setosa'],
...
 ['6.3', '2.5', '5.0', '1.9', 'Iris-virginica'],
 ['6.5', '3.0', '5.2', '2.0', 'Iris-virginica'],
 ['6.2', '3.4', '5.4', '2.3', 'Iris-virginica'],
 ['5.9', '3.0', '5.1', '1.8', 'Iris-virginica']]
```

## Create a Data Science Project Using the Cookiecutter

### Install the Cookiecutter package.
```bash
pip install cookiecutter
```

### Use the Cookiecutter to create a Data Science Project from the template repository.
```bash
cookiecutter https://github.com/faranalytics/data_science_project_cookiecutter.git
```

### Change directory into the repository's project directory.
This is the top-level directory of a conventional Python package.
```bash
cd <project_name>
```

### Activate your environment if you are using a package manager (e.g., conda).
```bash
conda activate <your-environment>
```

### Install the package in editable mode.  
An editable install, also known as a development install, will make changes to your package modules immediately available when you restart your kernel.
```bash
pip install -e .
```

## Dependencies
You can add dependencies to your project by modifying the `depdencies` section of the `pyproject.toml`.  

### Include the Pandas package.
You can include the `pandas` package, for example, by adding it to the list of `dependencies`.

`pyproject.toml`
```python
...
dependencies = [
    "hatch", 
    "ipykernel", 
    "pandas>=2, <3"
    ]
...
```
Reinstall your environment after specifying a new dependency.
```bash
pip install -e .
```

## Pipelines
You can use `__main__.py` in order to define your project's pipeline.  Once your package is installed and your pipeline is defined in your `__main__.py` module, you can run your package's pipeline using the `-m` option.
```bash
python -m <your-package-name>
```

## Publish
You can [publish](https://hatch.pypa.io/1.9/publish/) your package like you would publish an ordinary Python package.  If you install your package from PyPI you can import your results from the results sub-package.

### Install your package from PyPI.
```bash
pip install <your-package-name>
```

### Import the iris dataset from the results sub-package.
```python
from package.results import iris

iris
```
```python
[['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'],
 ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'],
 ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa'],
 ...]
```