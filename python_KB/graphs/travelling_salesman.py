#!usr/bin/env python

import random
import math
import networkx as nx
import matplotlib.pyplot as plt
from pyprocessing import *

class Node():
	def __init__(self, index):
		self.ID = index
		self.children = [] #array of tuples with child node and associated distance
		self.visited = False
		self.x = random.randint(0,500)
		self.y = random.randint(0,500)

class Search():
	def __init__(self,matrix):
		self.goal = None
		self.path = []
		self.pathCost = 0
		self.matrix = matrix
		self.vertQueue = []

	def findPath(self,node,goal):
		node[0].visited = True
		self.path.append(node)
		if node == goal:
			return
		else:
			neighbors = []
			for adj in self.matrix[node[0].ID]:	
				neighbors.append(adj)
			lowest_cost =  min(neighbors, key = lambda t: t[1])
			if lowest_cost[0].visited == False:
				self.pathCost += lowest_cost[1]
				self.findPath(min(self.matrix[node[0].ID]),goal)
			else:
				print "uh oh!"
				neighbors.remove(lowest_cost)
							
	def suckySearch(self,node,goal):
		node.visited = True
		self.path.append(node)
		if node == goal:
			return
		else:
			#copy matrix column
			copy = self.matrix[node.ID]
			self.suckySearch(self.getMin(copy),goal)
	
	def getMin(self,adjacent):
		low = (None,None,100000.0)
		cpy = adjacent
		for tup in cpy:
			if tup[2] < low[2]:
				if tup[1].visited == False:
					#print adjacent[0][0].ID, tup[2], low[2]
					low = tup
			#print tup[2]
		if low[0] == None:
			return self.goal
		else:
			#print "getMin:", low[1], "cost:", low[2]
			self.pathCost += low[2]
			return low[1]			
						
	def travel(self,node,goal):
		self.path.append(node)
		copy = self.matrix[node.ID]
		if node == goal:
			if node.visited == True:
				return 			
			else:
				node.visited = True
				self.travel(self.getMin(copy),goal)
		else:
			node.visited = True
			self.travel(self.getMin(copy), goal)
			

def makeGraph():
	pass

def readGraph():
	pass

def calcDistance(node1,node2):
	return math.sqrt((math.pow((abs(node1.x - node2.x)),2)) + (math.pow((abs(node1.y - node2.y)),2))) 

def defaultGraph():
	#returns an adjacency matrix of size n
	#nodes are randomly connected to one another at random distances
	graph = []
	for i in range(0,input("Enter number of vertices: ")):
		graph.append(Node(i))
	matrix = []
	for node in graph:
		adjacent = []
		for adj in graph:
			if node != adj:	
				dist = calcDistance(node,adj)
				adjacent.append((node, adj, dist))
		matrix.append(adjacent)
	return matrix, graph

def createGraph():
	g = raw_input("Would you like to (1) make your own graph, (2) read in a graph file, or (3) use the default graph? ")
	if g == "1":
		makeGraph()
	elif g == "2":
		readGraph()
	elif g == "3":
		matrix, graph = defaultGraph()
		search = Search(matrix)
		return search, matrix, graph
	else:
		print "Unrecognized input"

def showGraph(matrix):
	g = nx.DiGraph()
	for node in matrix:
		for adj in node:
			#adj[0] is parent node, adj[1] is child node, adj[2] is distance/cost
			g.add_weighted_edges_from([(adj[0].ID, adj[1].ID, adj[2])])
	nx.draw_shell(g)
	plt.show()
'''
def setup():
	size(500,500)
	noStroke()

def draw():
	background(0)
	matrix, graph = defaultGraph()
	for node in graph:
		fill(255)
		rect(node.x,node.y,10,10)	
'''
def main():
	search, matrix, graph = createGraph()
	randomSearchTask = random.choice(random.choice(matrix))
	print "Searching for optimal path from", randomSearchTask[0].ID, "to", randomSearchTask[0].ID, "ensuring all nodes are visited."
	search.start = randomSearchTask[0]
	search.goal = randomSearchTask[0]
	search.travel(search.start, search.goal)
	
	#search.findPath(matrix[0][0],matrix[9][0])
	'''
	print "Path:"
	for node in search.path:
		print "Node: ", node.ID, "X: ", node.x, "Y: ", node.y
	'''
	print "Total cost:", search.pathCost 
	if raw_input("Display graph? (y/n): ") == "y":
		#showGraph(matrix)
	#run()
		size(500,500)
		rectMode(CENTER)
		node_size = 3
		for node in graph:
			if node == search.start:
				fill(0,255,0)
				node_size = 7
			else:	
				node_size = 3
				fill(0)
			rect(node.x, node.y, node_size, node_size)
		'''
		for adj in matrix:
			for edge in adj:
				fill(0)
				line(edge[0].x, edge[0].y, edge[1].x, edge[1].y) 
		'''
		for i in range(0,len(search.path)-1):
			#rect(search.path[i].x, search.path[i].y, 10, 10)
			line(search.path[i].x, search.path[i].y, search.path[i+1].x, search.path[i+1].y)
		run()

if __name__=="__main__":
	main()
