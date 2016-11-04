#!usr/bin/env python

def ui(v,e):
	quit = False
	while not quit:
		print "\n"
		userInput = raw_input("What would you like to do? (hint: enter HELP for usage instructions) ")
		if userInput == "HELP":
			print "Commands: HELP, QUIT, VERTS, LIST, BFS, DFS"
		elif userInput == "QUIT":
			quit = True
		elif userInput == "VERTS":
			print "\n Verticies in adjacency list: ",",".join(v)
		elif userInput == "LIST":
			print "\n Adjacency list:"
			for item in e:
				print "Vertex:", item[0], " Neighbors:", ",".join(item[1])
		elif userInput == "BFS":
			print "\n BFS:"
			print BFS(e)
		else:
			print "\n Unrecognized command."		

def BFS(adjList):
	return 0

def parse(raw):
	clean = []
	string = ""
	for char in raw:
		if char == " ":
			if string != "":
				clean.append(string)
				string = ""
		else:
			string += char
	if string != "":
		clean.append(string)
	return clean

def getArgs():
	v = raw_input("Enter vertices, separated by spaces: ")
	verts = parse(v)	
	edges = []
	for vert in verts:
		e = raw_input("Specify " + vert + "'s adjacent vertices:")
		edges.append((vert,parse(e)))
	return verts,edges

def main():
	v,e = getArgs()
	print "Adjacency List successfully created!"
	ui(v,e)

if __name__=="__main__":
	main()
