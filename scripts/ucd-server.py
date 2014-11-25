#!/usr/bin/env python

# -*- coding: utf-8 -*-

import flask
from flask_cors import cross_origin 

import logging

import cooperhewitt.unicode.names as names
import cooperhewitt.flask.http_pony as http_pony

app = http_pony.setup_flask_app('UCD_SERVER')

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})

@app.route('/', methods=['GET', 'POST'])
@cross_origin(methods=['GET', 'POST'])
def lookup():

    try:

        if flask.request.method == 'POST':
            input = flask.request.form['string']
        else:
            input = flask.request.args.get('string', None)

    except Exception, e:
        logging.error("failed to get input because %s" % e)
        flask.abort(400)

    if not input:
        logging.error("Missing input")
        flask.abort(400)

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
