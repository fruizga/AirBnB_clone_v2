#!/usr/bin/python3
""" starts a Flask web application:

The default value of text is “is cool”

You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def StartAPI():
    """ Starts on port :5000 """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display /hbnb """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def CisFun(text):
    """ c is fun """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_IsCool(text="is cool"):
    """ python is cool """
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
