#!usr/bin/env python

class Graph():
	def __init__(self,nodes):
		self.nodes = nodes
		self.BFS_path = []
		self.DFS_path = []
		self.queue = []

	def BFS(self,start,end):
		self.queue.append(start)
		while self.queue != []:
			self.BFS_path.append(self.queue[0].ID)
			for child in self.queue[0].children:
				if child == end:
					print "Path found!"
					self.BFS_path.append(child.ID)
					return self.BFS_path
				else:
					self.queue.append(child)
			self.queue.pop(0)
		return self.BFS_path
	
	def DFS(self,start,end):
		self.DFS_path.append(start.ID)
		if start == end:
			print "Path found!"
			return
		else:
			for child in start.children:
				self.DFS(child,end)					
	
class Node():
	def __init__(self,name):
		self.ID = name
		self.parents = []
		self.children = []
	
	def addEdges(self,edges):
		for edge in edges:
			if edge[0].ID == self.ID:
				self.children.append(edge[1])
			elif edge[1].ID == self.ID:
				self.parents.append(edge[0])

def createNodes():
	nodes = list(raw_input("Enter the nodes in the graph, separated by spaces:"))
	nodeList = parse(nodes)
	verts = []
	for node in nodeList:
		verts.append(Node(node))
	return verts

def parse(parseme):
	parsed = []
	string = ""
	while parseme != []:
		if parseme[0] == " ":
			parseme.pop(0)
			parsed.append(string)
			string = ""
		else:
			string += parseme.pop(0)
	if string != " " and string != "":
		parsed.append(string)
	return parsed
	
def createEdges(nodes,graph):
	edgeList = []
	for node in nodes:
		edges = list(raw_input("Specify the direct connections from node " + node.ID + ", separated by spaces:"))
		if edges != []:
			edgeNodes = parse(edges)
			for edge in edgeNodes:
				for node2 in graph.nodes:				
					if edge == node2.ID:
						edgeList.append((node,node2))
	return edgeList

def main():
	node_list = createNodes()
	g = Graph(node_list)
	edge_list = createEdges(node_list,g)
	for node in g.nodes:
		node.addEdges(edge_list)
	start = raw_input("Enter starting node: ")
	end = raw_input("Enter goal node: ")
	for node in g.nodes:
		if node.ID == start:
			start = node
		elif node.ID == end:
			end = node	
	print "\n BFS:"
	path = g.BFS(start,end)
	print " --> ".join(path)
	print "\n DFS:"
	g.DFS(start,end)
	print " --> ".join(g.DFS_path)
	
if __name__=="__main__":
	main()
