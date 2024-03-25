#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Display 'HBNB'
    /c/<text>: Display C, followed by the value of the text
    /python/<text>: Display Python, followed the value of the text.
                    The default value of <text> is 'is cool'
    /number/<n>: Display 'n is a number' only if n is an integer'
    /number_template/<n>: Display HTML page only if n is an integer
                        H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by a formatted value of the <text>"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text='is cool'):
    """Display Python followed by a formatted value of <text>
    otherwise 'is cool'"""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display HTML page only if n is an integer inside H1 tag in the body
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
