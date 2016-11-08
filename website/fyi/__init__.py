#!/usr/bin/env python2

from flask import Flask
from flask_autodoc import Autodoc

from os import environ

host = "http://localhost:80"
app = Flask(__name__, static_url_path='')
auto = Autodoc(app)

import fyi.web
