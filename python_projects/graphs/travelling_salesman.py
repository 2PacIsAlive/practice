#!usr/bin/env python

import re
import glob
import random
import math
#import ipdb
#breakP = ipdb.set_trace
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
		self.mutatedPath = None		

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
	
	def combineChildren(self,path1,path2):
		newPath = []
		newPath.append(path1[0])
		print "\ncombining children..."
		for node in newPath:
			if len(newPath) == len(path1) - 1:
				print "last item, adding goal"
				print self.goal.ID
				newPath.append(self.goal)
			else:
				path1_exists = False
				path2_exists = False
				path1_index = self.findIndex(node,path1) + 1
				path2_index = self.findIndex(node,path2) + 1
				if path1[path1_index] in newPath:
					print "can't add path 1: ", path1[path1_index].ID
					path1_exists = True
				if path2[path2_index] in newPath:
					print "can't add path 2: ", path2[path2_index].ID
					path2_exists = True
				if random.randint(0,11) > 3:
					if path1_exists == False:
						if path1[path1_index] == self.goal:
							if len(newPath) == len(path1) - 1:
								print "adding goal from path1"
								print path1[path1_index].ID
								newPath.append(path1[path1_index])
							else:
								print "tried to add goal from path1, not ready"
								print path2[path2_index].ID
								newPath.append(path2[path2_index])
						else:
							print "adding from path1"
							print path1[path1_index].ID
							newPath.append(path1[path1_index])
					else:
						print "path 1 next already in path, adding path2 next instead"
						print path2[path2_index].ID
						if path2_exists == False:
							newPath.append(path2[path2_index])
						else:	
							#find random node that is not in path
							found = False
							for node in path2:
								if found == False:
									if node not in newPath:
										newPath.append(node)
										found = True
				else:
					if path2_exists == False:
						if path2[path2_index] == self.goal:
							if len(newPath) == len(path1) - 1:
								print "adding goal from path2"
								print path2[path2_index].ID
								newPath.append(path2[path2_index])
							else:
								"tried to add goal from path2, not ready"
								print path2[path2_index].ID
								newPath.append(path1[path1_index])
						else:
							print "adding from path2"
							print path2[path2_index].ID
							newPath.append(path2[path2_index]) 
					else:
						print "path 2 next already in path, adding path1 next instead"
						print path1[path1_index].ID
						if path1_exists == False:
							newPath.append(path1[path1_index])
						else:
							#find random node that is not in path
							found = False
							for node in path1:
								if found == False:
									if node not in newPath:
										newPath.append(node)
										found = True
			if len(newPath) == len(path1):
				print "new path:", self.calcDist(newPath)
				for node in newPath:
					print node.ID
				return newPath

	def calcDist(self,path):
		index = 0
		dist = 0
		for node in path:
			dist += calcDistance(path[index],path[index+1])
			print "dist:", dist
		return dist
	
	def mutate(self,path,original,newPath):
		possibleVerts = [x for x in path if x != self.goal]
		gene = random.choice(possibleVerts)
		possibleVerts.remove(gene)
		new = random.choice(possibleVerts)
		newLoc = self.findIndex(new,path)
		geneLoc = self.findIndex(gene,path)
		path[newLoc] = gene
		path[geneLoc] = new
		#print "\nmutated path:"
		#for node in path:
		#	print node.ID
		if len(newPath) < 100:
			newPath.append((path,self.calcDist(path)))
			self.mutate(original, original, newPath)
		else:
			self.mutatedPath = min(newPath, key = lambda t: t[1])
			return

	def geneticAlgorithm(self,start,goal):
		try:
			self.genRandomPaths(start,goal)
		except RuntimeError:
			print "Recursion depth exceeded, only", len(self.randompaths), "random paths created."
			pass #take what we can get
		child1 = min(self.randompaths, key = lambda t: t[1])
		print "child1", child1[1]
		for node in child1[0]:
			print node.ID
		self.randompaths.remove(child1)
		child2 = min(self.randompaths, key = lambda t: t[1])
		print "\nchild2", child2[1]
		for node in child2[0]:
			print node.ID	
		print
		combination = self.combineChildren(child1[0],child2[0])
		print "\nunmutated path:"
		for node in combination:
			print node.ID
		self.mutate(combination,combination,[])
		self.path = self.mutatedPath[0]
		print "mutated path cost:", self.mutatedPath[1]
		#self.path = min(self.mutate(combination), key = lambda t: t[1])
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
	g = raw_input("Would you like to (1) make your own graph, (2) read in a graph file, or (3) create a random graph? ")
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
