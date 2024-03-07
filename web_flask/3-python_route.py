#!/usr/bin/python3
""" simple single server """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_route():
    """ display greeting """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb_route():
    """ handles route /hbnb and returns string """
    return "HBNB"


@app.route('/c/<text>')
def text_route(text):
    """ handles route /c/<text> returns string replacing _ with spaces """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ handles route /python/<text>, optional parameter, defaults is cool """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
