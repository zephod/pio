# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import render_template, flash, g, jsonify
from app import app
import pio

# for debug
from pprint import pformat
from flask import request
# For reference:
#flash( pformat({x:request.__getattr__(x) for x in dir(request)}) ,'info')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/',methods=['post'])
def json_post():
    data = request.form
    pio.setChannel( int(data['channel']), (data['value']) )
    return ''

@app.route('/poll/')
def json_poll():
    data = pio.getState()
    return jsonify(data)

