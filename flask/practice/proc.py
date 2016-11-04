from practice import celery, githubApi

from os import system
from glob import glob
from json import dumps

@celery.task
def getContent(path):
    system('git checkout ' + path['branch'])
    system('git pull origin ' + path['branch'])
    langs = [folder for folder in glob('../*') if 'KB' in folder]
    topicsByLang = {lang: topic for lang, topic in [(folder, glob(folder + '/*')) for folder in langs]}
    return dumps(topicsByLang)
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
