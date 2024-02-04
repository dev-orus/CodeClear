# ---------------------------
#
# CodeClear - @2024
#
# ---------------------------
#
# Server - Made with Flask
#
# ---------------------------

from flask import Flask, request, jsonify, render_template
import os
from os.path import join
import yaml
from yaml.loader import SafeLoader

parent = os.path.dirname(os.path.dirname(__file__))

app = Flask(__name__, static_folder=join(parent, 'Client', 'build'))

@app.route('/', methods=['GET'])
def get_example():
    return render_template()

if __name__ == '__main__':
    with open(join(parent, 'server.yaml'))as f:
        config = yaml.load(f, Loader=SafeLoader)
    app.run(debug=config['port'], port=config['port'], host=config['host'])