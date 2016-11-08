from fyi import app, auto

from flask import render_template, request
from datetime import datetime
from glob import glob

@app.route('/', methods=['GET'])
@auto.doc()
def indexPage():
    languages = glob('../languages/*/')
    projects = []
    for language in languages:
        projects += glob(language + '*/')
    return render_template(
        "index.html",
        projects=list(set([project.split('/')[3] for project in projects])),
        languages=[language.split('/')[2] for language in languages]
    )

@app.route('/languages/<string:language>', methods=['GET'])
@auto.doc()
def languagePage(language):
    projects = glob('../languages/' + language + '/*/')
    return render_template(
        "language.html",
        language=language,
        projects=list(set([project.split('/')[3] for project in projects])),
    )

