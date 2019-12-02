import os
import sys
sys.path.append("../../")

import argparse
from flask import Flask, request, abort, jsonify

from iris.api import IrisAPI

# parse args
parser = argparse.ArgumentParser(description='Runs example web API.')
parser.add_argument('--load', help='load model at start', dest='load', action='store_true')
parser.set_defaults(load=True)
args = parser.parse_args()

# instantiate flask app
app = Flask(__name__)
iris_api = IrisAPI()
if args.load:
    iris_api.instantiate()


@app.route("/init_predict", methods=['GET'])
def init_predict():
    """Initializes the iris api"""

    iris_api.instantiate()

    return 'Iris API loaded!'


@app.route("/predict", methods=['POST'])
def predict():
    """
    Loads the iris array argument of HTTP GET request,
    predicts classes distribution from it. Returns a JSON.
    """
    payload = request.get_json(force=True, silent=True)
    x = payload["x"]
    x = iris_api.preprocess(x)
    y_pred = list(iris_api.predict(x))

    return jsonify(y_pred=y_pred)


if __name__ == "__main__":
    app.run(debug=False, host='localhost', port=8198)
    # /!\ Warning /!\
    # When debug set to True, TensorFlows crashes because of asynchronous model.
