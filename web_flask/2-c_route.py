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
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """function for text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)