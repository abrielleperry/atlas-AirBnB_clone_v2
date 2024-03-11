#!/usr/bin/python3
""" simple single server """
from flask import Flask, render_template, request
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
