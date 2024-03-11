#!/usr/bin/python3
""" simple single server """
from flask import Flask, render_template, request
from models import storage
app = Flask(__name__)


@app.route('/states_list')
def get_db():
    """ display greeting """
    states = sorted(list(storage.all("State").values()),
                    key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_db(exception=None):
    """ teardown database """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
