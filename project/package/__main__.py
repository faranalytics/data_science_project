import pathlib
import pickle
from pprint import pprint
import papermill as pm
from package.results import RESULTS_PATH

pm.execute_notebook(
    pathlib.Path(__file__).parent.resolve().joinpath("methods/notebooks/main.ipynb"),
    None,
)

if RESULTS_PATH.joinpath('iris.data.pkl').exists():
    with open(RESULTS_PATH.joinpath("iris.data.pkl"), "rb") as f:
        iris = pickle.load(f)
        pprint(iris[0:10])