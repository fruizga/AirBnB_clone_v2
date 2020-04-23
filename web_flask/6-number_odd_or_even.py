#!/usr/bin/python3
""" starts a Flask web application:

H1 tag: “Number: n is even|odd” inside the tag BODY

"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def StartAPI():
    """ Starts on port :5000 """
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displaying /hbnb """
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

@app.route('/number/<int:n>', strict_slashes=False)
def CHeckNumInt(n):
    """ Evaluates if num is int """
    return ("{:d} is a number".format(n))

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_view(n):
    """html view for numbers"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def Even_Odd(n):
    """ html view for even and odds """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
