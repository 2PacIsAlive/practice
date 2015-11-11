#!usr/bin/env python

import re
import glob
import random
import math
import ipdb
breakP = ipdb.set_trace
#import networkx as nx
#import matplotlib.pyplot as plt
from pyprocessing import *

class Node():
	def __init__(self, index):
		self.ID = index
		self.children = [] #array of tuples with child node and associated distance
		self.visited = False
		self.x = random.randint(0,500)
		self.y = random.randint(0,500)

class Search():
	def __init__(self,matrix, graph):
		self.goal = None
		self.path = []
		self.randompaths = []
		self.randomPathCost = 0
		self.pathCost = 0
		self.matrix = matrix
		self.graph = graph
		self.vertQueue = []
		self.randomChoice = None
		self.numChildren = 50

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

	def remainingUnvisited(self,adjacent):
		for node in adjacent:
			if node[1] != self.goal:
				if node[1].visited == False:
					return True
		return False	

	#this function has flawed logic!!!
	def getRandom(self,adjacent):
		cpy = list(filter((lambda x: x[1].visited == False),adjacent))
		if cpy == []:
			self.randomChoice = self.goal
			return
		rand = random.choice(cpy)
		if rand[1] == self.goal:
			if self.remainingUnvisited(cpy) == True:
				#print "\nOPTIONS REMAIN:"
				#for item in cpy:
				#	print item[1].ID, item[1].visited
				#cpy.remove(rand)
				self.getRandom(cpy)
			else:
				#print "\nNO MORE REMAINING OPTIONS, SELECTING GOAL:"
				#print rand[1].ID, rand[1].visited
				self.randomPathCost += rand[2]
				self.randomChoice = rand[1]
				return
		else:
			if rand[1].visited == False:
				#print "\nSELECTING RANDOM"
				#print rand[1].ID
				self.randomPathCost += rand[2]
				self.randomChoice = rand[1]
				return
			else:
				#print "ALREADY VISITED"
				#print rand[1].ID, rand[1].visited
				#cpy.remove(rand)
				self.getRandom(cpy)

	def genRandomPaths(self,node,goal):
		self.path.append(node)
		copy = self.matrix[node.ID]
		if node == goal:
			if node.visited == True:
				#print "Path found!"
				#for x in self.path:
				#	print x.ID
				self.randompaths.append((self.path,self.randomPathCost))
				self.randomPathCost = 0
				self.path = []
				for i in self.graph:
					i.visited = False
				if len(self.randompaths) == self.numChildren:
					return
				else:
					self.genRandomPaths(node,goal)
			else:
				node.visited = True
				self.getRandom(copy)
				self.genRandomPaths(self.randomChoice, goal)
		else:
			node.visited = True
			self.getRandom(copy)
			self.genRandomPaths(self.randomChoice, goal)
	
	def findIndex(self,node,path):
		index = 0
		for item in path:
			if item == node:
				return index
			index += 1
		print "Node not found."

	def add_to_path(self, index, list1, list2, newPath):
		if newPath == []:
			newPath.append(self.start)
			return newPath
		if len(newPath) == len(list1)-1:
			newPath.append(self.goal)
			return newPath
		if index == len(list1)-1:
			newIndex = findIndex(list2[index], list1)
			newPath.append(list1[newIndex+1])
			return newPath
		if list1[index+1] not in newPath:
			newPath.append(list1[index+1])
			return newPath
		else:
			newPath.append(list2[index+1])
			return newPath
	
	def combineChildren(self,path1,path2):
		size = len(path1)
		#path1 = [x for x in path1 if x != self.goal]
		#path2 = [x for x in path2 if x != self.goal]
		newPath = []
		index = 0
		while len(newPath) < size:
			if random.randint(0,1) == 0:
				newPath = self.add_to_path(index, path1, path2, newPath)
			else:	
				newPath = self.add_to_path(index, path2, path1, newPath)
		return newPath
		

	'''
	#BROKEN
	def combineChildren(self,child1,child2):
		finalSize = len(child1) 
		child1 = [x for x in child1 if x != self.goal]
		child2 = [x for x in child2 if x != self.goal]
		newPath = []
		newPath.append(self.start)
		for node in child1:
			if len(newPath) != finalSize-1:
				if random.randint(0,1) == 1: 
					index = self.findIndex(node, child2)
					if child2[index+1] not in newPath:
						newPath.append(child2[index+1])
					else:
						index = self.findIndex(node, child1)
						newPath.append(child1[index+1])	
				else:
					index = self.findIndex(node, child1)
					if child1[index+1] not in newPath:
						newPath.append(child1[index+1])
					else:
						index = self.findIndex(node, child2)
						newPath.append(child2[index+1])
			else:
				break
		newPath.append(self.goal)
		return newPath
	'''

	def geneticAlgorithm(self,start,goal):
		try:
			self.genRandomPaths(start,goal)
		except RuntimeError:
			print "Recursion depth exceeded, only", len(self.randompaths), "random paths created."
			pass #take what we can get
		child1 = min(self.randompaths, key = lambda t: t[1])
		self.randompaths.remove(child1)
		child2 = min(self.randompaths, key = lambda t: t[1])
		self.path = self.combineChildren(child1[0],child2[0])
		#self.path = child1[0] 

def makeGraph():
	pass

def readGraph():
	files = glob.glob("data/*")
	for f in files:
		print f
	data = raw_input("Choose your data file: ")
	fo = open("data/"+data+".txt")
	#fo.read()
	lines = []
	for line in fo:
		vals = []
		num = ""
		count = 0
		for char in line:
			if char == " ":
				vals.append(num)
				num = ""
			else:
				num += char
		vals.append(num[:-1])
		lines.append(vals)
	#num = num[:-1]
	#vals.append(num)
	#lines.append(vals)
	fo.close()
	graph = []
	for line in lines:		
		node = Node(int(line[0]))
		node.x = int(line[1])
		node.y = int(line[2])
		graph.append(node)
	matrix = adjacencyMatrix(graph)
	return matrix, graph
	
def calcDistance(node1,node2):
	return math.sqrt((math.pow((abs(node1.x - node2.x)),2)) + (math.pow((abs(node1.y - node2.y)),2))) 

def adjacencyMatrix(graph):
	matrix = []
	for node in graph:
		adjacent = []
		for adj in graph:
			if node != adj:
				dist = calcDistance(node,adj)
				adjacent.append((node, adj, dist))
		matrix.append(adjacent)
	return matrix


def defaultGraph():
	#returns an adjacency matrix of size n
	#nodes are randomly connected to one another at random distances
	graph = []
	for i in range(0,input("Enter number of vertices: ")):
		graph.append(Node(i))
	matrix = adjacencyMatrix(graph)
	return matrix, graph

def saveGraph(matrix, graph):
	files = glob.glob("data/*")
	print "Preexisting graphs:"
	for f in files:
		print f
	name = raw_input("Enter the name of the new graph: (using the same name will overwrite the existing graph) ") + ".txt"
	fo = open("data/"+name,"w")
	#for adj in matrix:
	#	for connection in adj:
	#		line = str(connection[0].ID) + " " + str(connection[0].x) + " " + str(connection[0].y) + " " + str(connection[1].ID) + " "  + str(connection[1].x) + " " + str(connection[1].y) + "\n"
	#		fo.write(line)i
	for node in graph:
		line = str(node.ID) + " " + str(node.x) + " " + str(node.y) + "\n"
		fo.write(line)
	fo.close()
	print "File written."

def createGraph():
	g = raw_input("Would you like to (1) make your own graph, (2) read in a graph file, or (3) use the default graph? ")
	if g == "1":
		makeGraph()
	elif g == "2":
		matrix, graph = readGraph()
		search = Search(matrix, graph)
		return search, matrix, graph
	elif g == "3":
		matrix, graph = defaultGraph()
		search = Search(matrix, graph)
		if raw_input("Would you like to save the randomly generated graph? (y/n) ") == "y":
			saveGraph(matrix, graph)
		return search, matrix, graph
	else:
		print "Unrecognized input"
		createGraph()

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
	algo = raw_input("Which algorithm would you like to use? ")
	if algo == "nearest neighbor": 
		search.travel(search.start, search.goal)
		print "Total cost:", search.pathCost 
	elif algo == "genetic":
		search.geneticAlgorithm(search.start, search.goal)
		#print "Fitness scores:"
		#for path, score in search.randompaths:
		#	print score	
	#search.findPath(matrix[0][0],matrix[9][0])
	'''
	print "Path:"
	for node in search.path:
		print "Node: ", node.ID, "X: ", node.x, "Y: ", node.y
	'''
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
