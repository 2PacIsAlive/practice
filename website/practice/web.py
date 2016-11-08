from practice import app, auto
from proc import getContent

from flask import render_template, request
from datetime import datetime
from glob import glob

@app.route('/', methods=['GET'])
@auto.doc()
def indexPage():
    timestamp = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    print '[' + timestamp + '] ' + str(request.user_agent) # TODO log this instead
    languages = glob('../languages/*/')
    projects = []
    for language in languages:
        projects += glob(language + '*/')
    return render_template(
        "index.html",
        projects=list(set([project.split('/')[3] for project in projects])),
        languages=[language.split('/')[2] for language in languages]
    )
'''
@app.route('/<string:branch>/<string:lang>/<string:file_>', methods=['GET'])
@auto.doc()
def repoPage(branch, lang, file_):
    task = getContent.delay(branch + '/' + lang + '/' + file_)
    obj = task.get()

    if path.isRoot:
        return render_template(
            "root.html",
            directories = obj['dirs'],
            files = obj['files'],
            readme = obj['readme']
        )
    elif path.isDirectory:
        return render_template(
            "dir.html",
            files = obj['files'],
            readme = obj['readme']
        )
    elif path.isFile:
        return render_template(
            "file.html",
            content = obj['content']
        )

    else:
        return render_template('500.html')
'''
