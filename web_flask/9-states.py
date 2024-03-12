#!/usr/bin/python3
""" simple single server """
from flask import Flask, render_template, request
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ display greeting """
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id():
    """ display greeting """
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close_db(close):
    """ teardown database """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
