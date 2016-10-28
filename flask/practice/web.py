from practice import app, auto
from proc import getContent

from flask import render_template, request
from datetime import datetime

@app.route('/', methods=['GET'])
@auto.doc()
def indexPage():
    timestamp = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    print '[' + timestamp + '] ' + str(request.user_agent) # TODO log this instead
    return render_template("index.html")

@app.route('/<string:branch>/<string:file_>', methods=['GET'])
@auto.doc()
def repoPage(branch, file_):
    task = getContent.delay(branch + '/' + file_)
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
