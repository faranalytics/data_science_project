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

You can clone this repository, explore, and modify it to meet your needs or [create a project using the Cookiecutter](#create-a-data-science-project-using-the-cookiecutter).
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
    ├── pyproject.toml ⬅ The project is configured to use the Hatch project manager.
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

### Open the `package/methods/notebooks/main.ipynb` notebook and run the cells.

Import the path of each sub-package.
```python
from package.materials import MATERIALS_PATH
from package.methods import METHODS_PATH
from package.results import RESULTS_PATH
```

Import a utility function from the methods sub-package.
```python
from package.methods.utils import say_hello

say_hello()
```

Read data from the `MATERIALS_PATH`, transform it into a list of lists, and write the data to the `RESULTS_PATH`.
```python
from pprint import pprint
import pickle
data = [
    line.strip().split(",")
    for line in open(MATERIALS_PATH.joinpath("iris/iris.data")).readlines()[:-1]
]

pickle.dump(data, open(RESULTS_PATH.joinpath("data.pkl"), "wb"))
```
## Create a Data Science Project Using the Cookiecutter

### Install the Cookiecutter package.
```bash
pip install cookiecutter
```

### Use the Cookiecutter to create a Data Science Project from the cookiecutter branch.
```bash
cookiecutter https://github.com/faranalytics/data_science_project.git --checkout cookiecutter
```

### Complete the Cookiecutter form.
```bash
  [1/2] project_name (project): my_project_name
  [2/2] package_name (package): my_package_name
```
You can give your project and package the same name.

### Change directory into the repository's project directory.
This is the top-level directory of a conventional Python package.
```bash
cd <my_project_name>
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
You can add dependencies to your project by modifying the `dependencies` section of the `pyproject.toml`.  

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
You can publish your package by following the instructions in the [tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).  Alternatively, you can use the [Hatch](https://hatch.pypa.io/latest/) CLI tool.