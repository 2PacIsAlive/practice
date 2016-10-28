from practice import celery, githubUrl

from requests import get

@celery.task
def getContent(path):
    meta = path.split('/')
    branch = meta[1]
    dirs = []
    if len(meta[1:]) > 1:
        for directory in meta[1:-1]:
            dirs.append(directory)
        filename = meta[-1]
    content = get(githubUrl + path)
    return content
