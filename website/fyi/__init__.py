#!/usr/bin/env python2

from flask import Flask
from flask_autodoc import Autodoc

from os import environ

host = "http://localhost:8000"
#host = "http://programming.fyi"
app = Flask(__name__, static_url_path='')
app.config['HOST'] = host
auto = Autodoc(app)

import fyi.web
