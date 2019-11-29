"""API (application programming interface)"""

import numpy as np
from iris.model.svm import IrisSVM
from iris.settings import settings


MODEL_PATH = settings["dumps"]["iris_svm_model_path"]


class IrisAPI(object):
    """
    API for score prediction from Iris data. Example.
    Needs to initialize the API through the 'load' method before using it.
    """

    def __init__(self):
        self.loaded = False
        self.model = None
        self.model_path = None

    def instantiate(self, model_path=MODEL_PATH, force=False):
        """
        Loads the model. After this call, RAM will be use in CPU.

        Parameters
        ----------
        force : boolean, default=False
            Whether to load the model even if previously loaded.
            Might be useful if the model saved on disk has changed.
        """
        if force or not self.loaded:
            self.model = IrisSVM()
            self.model.load(model_path)
            self.model_path = model_path
            self.loaded = True

    def preprocess(self, x_array):
        """
        Preprocess an array representing the input data.
        """
        return x_array

    def check_preprocess(self, x_array):
        """
        Checks if the size of an array fits the requirements of the model.
        Note that we have no insurance that x corresponds to the exact preprocessing
        done in preprocess method.

        Parameters
        ----------
        x: array
            Array to be checked

        Results
        -------
        check: boolean
            Whether the shape is correct.
        """

        check = x_array.shape == (4,)

        return check

    def predict(self, x_array):
        """
        Predicts score from an iris data loaded as array.

        Parameters
        ----------
        x: array, shape = [4,]
            Array representing the iris unitary data, directly usable by a model

        Results
        -------
        score: float
        """

        return self.model.predict(np.asarray([x_array]))[0]
