#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def print_states_list():
    """ HTML view for states """
    list_s = storage.all('State')
    return render_template('8-cities_by_states.html', list_s=list_s)


@app.teardown_appcontext
def close_storage(self):
    """ Close and remove session
    """
    storage.close()


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000, debug=True)
