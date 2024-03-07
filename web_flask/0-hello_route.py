#!/usr/bin/python3
""" simple single server """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_route():
    """ display greeting """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
