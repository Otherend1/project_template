import os
import sys
import json
import urllib
import requests

from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_basicauth import BasicAuth


URL_BACK = 'http://localhost:8198'
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = "ANEODATA"
app.config['BASIC_AUTH_PASSWORD'] = "aneodata"
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)


@app.route('/', methods=['GET'])
@basic_auth.required
def index():
    """Main page. Do not need to manipulate templating but shown as an example."""
    args = {}
    
    return render_template('index.html', **args)


@app.route('/predict', methods=['GET', 'POST'])
@basic_auth.required
def predict():
    """
    Returns all other predictions as the unchanged json.
    """
    x = [float(v) for v in request.form.to_dict().values()]
    payload = json.dumps({"x": x})
    res = requests.post(URL_BACK+"/predict", data=payload)

    return jsonify(res.json())


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8123)
