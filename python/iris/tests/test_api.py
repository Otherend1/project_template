import os
import sys
sys.path.append("../../../python/")

import pytest
import numpy as np
from sklearn import datasets
from iris.api import IrisAPI
from iris.model.svm import IrisSVM
from iris.settings import settings


x_test = [
    np.asarray([5.1, 3.5, 1.4, 0.2]),
    np.asarray([4.7, 3.2, 1.3, 0.2]),
    np.asarray([4.9, 3. , 1.4, 0.2]),
]


class TestModel:
    def setup(self):
        self.model_path = "/tmp/model.joblib"
        
        # load dataset
        iris = datasets.load_iris()
        self.X, self.y = iris.data, iris.target

        # fit and save file
        self.model = IrisSVM()
        self.model.fit(self.X, self.y)
        self.expected_y_pred = self.model.predict(self.X[:3])

    def test_model_save(self):
        # define model path
        self.model.save(self.model_path)

        # check if model is saved
        assert os.path.exists(self.model_path), "model is not saved"
    
    def test_model_load_and_predict(self):
        # define model path
        self.model.load(self.model_path)
        y_pred = self.model.predict(self.X[:3])
        assert np.allclose(y_pred, self.expected_y_pred, atol=1e-2), "y_pred is not the expected one"


expected_y_pred = [
    np.asarray([0.9774138730403789, 0.014465799435594418, 0.008120327524026817]),
    np.asarray([0.9785255404934668, 0.013574219998230297, 0.007900239508302924]),
    np.asarray([0.969269655896652, 0.02158718405900436, 0.009143160044343544]),
]


class TestAPI:
    def setup(self):
        self.iris_api = IrisAPI()
        self.iris_api.instantiate()

    def test_model_load(self):
        # check if model is loaded
        loaded = self.iris_api.loaded
        assert loaded

    def test_model_path(self):
        # check model_path 
        model_path = self.iris_api.model_path
        expected_model_path = settings["dumps"]["iris_svm_model_path"]
        assert model_path == expected_model_path

    @pytest.mark.parametrize("x", x_test)
    def test_preprocessing(self, x):
        # check preprocessing
        x = self.iris_api.preprocess(x)
        assert self.iris_api.check_preprocess(x), "x is not at the right format"

    @pytest.mark.parametrize("x, expected_y_pred", list(zip(x_test, expected_y_pred)))
    def test_predict(self, x, expected_y_pred):
        # check prediction
        x = self.iris_api.preprocess(x)
        y_pred = self.iris_api.predict(x)
        assert np.array_equal(y_pred, expected_y_pred), "y_pred is not the expected one"
