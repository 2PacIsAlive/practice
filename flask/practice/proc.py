from practice import celery, githubApi 

from requests import get

@celery.task
def getContent(path):
    print githubApi.get_user().get_repos()
    return ""
    #meta = path.split('/')
    #branch = meta[1]
    #dirs = []
    #if len(meta[1:]) > 1:
    #    for directory in meta[1:-1]:
    #        dirs.append(directory)
    #    filename = meta[-1]
    #print githubUrl + path
    #content = get(githubUrl + path)
    #return content.text
