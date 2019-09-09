#!/usr/bin/python3
""" Import flask class """
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ Function to handle request """
    states = storage.all(State)
    dict_states = {}
    for _, value in states.items():
        dict_states[value.id] = value.name
    return render_template('7-states_list.html', states=dict_states)


@app.route('/cities_by_states')
def cities_states():
    """ Function to handle request cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/')
@app.route('/states/<id>')
def states_by_id(id=None):
    """ Function to handle request cities"""
    states = storage.all(State)
    if id is not None:
        class_id = "State." + id
        if class_id in states:
            return render_template('9-states.html', state=states[class_id])
        else:
            return render_template('9-states.html', state=None)
    dict_states = {}
    for _, value in states.items():
        dict_states[value.id] = value.name
    return render_template('7-states_list.html', states=dict_states)


@app.teardown_appcontext
def storage_close(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
