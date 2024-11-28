import pathlib
import pickle
RESULTS_PATH = pathlib.Path(__file__).parent

iris = None
if RESULTS_PATH.joinpath('iris.data.pkl').exists():
    with open(RESULTS_PATH.joinpath("iris.data.pkl"), "rb") as f:
        iris = pickle.load(f)