#!/usr/bin/python3
from flask import Flask
"""documentation calling flask"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function to return He llo HBNB"""
    return 'Hello HBNB!'

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """fucntion for HBNB"""
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """function for text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """function for python text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    try:
        n = int(n)
        return '{} is a number'.format(n)
    except ValueError:
        return 'Not a number'
        
