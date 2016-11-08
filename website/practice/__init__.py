#!/usr/bin/env python2

from flask import Flask
from flask_autodoc import Autodoc

from os import environ

host = "http://localhost:8000"
app = Flask(__name__, static_url_path='')

app.config['HOST'] = host
app.config['CELERY_ACCEPT_CONTENT'] = ['json', 'application/json', 'pickle']
app.config['CELERY_TASK_SERIALIZER'] = 'json'
app.config['BACKEND_URL'] = 'amqp://practice:' + environ['RBMQP'] + '@localhost//'
app.config['BROKER_URL'] = 'amqp://practice:' + environ['RBMQP'] + '@localhost//'
app.config['CELERY_TIMEZONE'] = 'America/Denver'

import practice.util
celery = util.make_celery(app)
auto = Autodoc(app)
import practice.web
import practice.proc
