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
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storage_close(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
