from practice import celery

from os import system
from glob import glob
from json import dumps

@celery.task
def getContent(path):
    #system('git checkout ' + path['branch'])
    #system('git pull origin ' + path['branch'])
    langs = [folder for folder in glob('../languages/*')]
    topics = {lang: topic for lang, topic in [(folder, glob(folder + '/*')) for folder in langs]}
    return dumps({
        "langs": langs,
        "topics": topics
    })
    #print githubApi.get_user().get_repos()
    #return ""
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
