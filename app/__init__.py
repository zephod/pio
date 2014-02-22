# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.pymongo import PyMongo

app = Flask(__name__,static_folder='../static')
app.config.from_object('app.configuration.DevelopmentConfig')

bs = Bootstrap(app) #flask-bootstrap

from app import views
