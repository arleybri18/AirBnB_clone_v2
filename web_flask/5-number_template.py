#!/usr/bin/python3
""" Import flask class """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """ Function to handle request """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """ Function to handle request to path /hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """ Function to handle request with a variable """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """ Function to handle request with a variable and data default """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:num>')
def numbers(num):
    """ Function to handle request with a variable with specified type """
    return '%d is a number' % num


@app.route('/number_template/<int:num>')
def numbers_temp(num):
    """ Function to handle request and render template"""
    return render_template('5-number.html', number=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
