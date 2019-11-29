"""SVM class to be trained on the iris dataset"""

from sklearn import svm
from joblib import dump, load


class IrisSVM():
    """SVM model designed for the iris dataset"""
    
    def __init__(self, gamma="scale", probability=True):
        """hyperparameters initialisation"""
        self.gamma = gamma
        self.probability = probability
        self.model = self.instantiate_model()

    def instantiate_model(self):
        """create model architecture"""
        model = svm.SVC(gamma=self.gamma, probability=self.probability)

        return model

    def fit(self, X, y):
        """train model"""
        self.model.fit(X, y)

    def predict(self, X):
        """predict on X"""
        return self.model.predict_proba(X)

    def save(self, model_path):
        """save model's weights"""
        dump(self.model, model_path)

    def load(self, model_path):
        """load model's weights"""
        self.model = load(model_path)
