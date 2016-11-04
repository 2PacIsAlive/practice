#!usr/bin/env python

import random
from pyprocessing  import *
from scipy.spatial import distance


class KMeansCluster:

    #grid = [x for x in range(50,275)] + [x for x in range(325,550)]
    grid = [x for x in range(50,550)]
    
    iteration = 0

    def __init__(self, num_centroids, num_objs):
        self.centroids = [{'x': random.choice(self.grid),        
                           'y': random.choice(self.grid), 
                           'r': random.randint(0,255),
                           'g': random.randint(0,255),
                           'b': random.randint(0,255),
                           'class': x }  for x in range(num_centroids)]
        self.objects   = [{'x': random.choice(self.grid), 
                           'y': random.choice(self.grid), 
                           'r': random.randint(0,255),
                           'g': random.randint(0,255),
                           'b': random.randint(0,255),
                           'class': None }  for x in range(num_objs)]

    def find_class(self, point, centroids):
        dst = [(distance.euclidean((point['x'],point['y']), (x['x'],x['y'])), x) for x in centroids]
        return min(dst, key = lambda x: x[0])

    def update(self):
        for point in self.objects:
            new_class = self.find_class(point, self.centroids)[1] 
            point['r'] = new_class['r']
            point['g'] = new_class['g']
            point['b'] = new_class['b']
            point['class'] = new_class['class']

    def recompute_centroids(self):
        for centroid in self.centroids:
            group = [x for x in self.objects if x['class'] == centroid['class']]
            centroid['x'] = sum([x['x'] for x in group]) / len([x['x'] for x in group])
            centroid['y'] = sum([x['y'] for x in group]) / len([x['y'] for x in group])

def setup():
    size(600,600)
    noStroke()

def draw():
    background(50)
    for point in cluster.objects:
        fill(point['r'], point['g'], point['b'])
        rect(point['x'], point['y'], 10, 10)
    cluster.update()
    cluster.recompute_centroids()
    #save('images/'+str(cluster.iteration+83)+'.png')
    cluster.iteration += 1

cluster = KMeansCluster(input("Clusters: "), input("Objects: "))
run() # for fun
