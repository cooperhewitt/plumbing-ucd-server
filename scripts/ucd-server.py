#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import logging

import cooperhewitt.unicode.names as names
import cooperhewitt.flask.http_pony as http_pony

app = http_pony.setup_flask_app('ATKINSON_SERVER')

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})

@app.route('/', methods=['GET'])
@cross_origin(methods=['GET'])
def lookup():

    input = flask.request.get('string')
    input = input.decode('utf-8')
    
    ref = names.lookup()
    chars = []

    for char in input:
        name = ref.name(char)
        chars.append((char, name))

    return flask.jsonify({'stat': 'ok', 'chars': chars})

if __name__ == '__main__':

    # app is defined above, remember
    http_pony.run_from_cli(app)
