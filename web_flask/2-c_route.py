#!/usr/bin/python3
""" starts a Flask web application2:

    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )

"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def StartAPI():
    """ Start on port :5000 """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display /hbnb """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def CisFun(text):
    """ change _ for """
    return ("C {}".format(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
