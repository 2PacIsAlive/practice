#!usr/bin/env python 

class Tree():
	def __init__(self,nodes,n):
		self.tree = nodes
		self.n = n
	
	def getChildren(self,node):
		#node is the index to the nodes array
		children = []
		c = 0
		while c < self.n:
			try:	
				index = self.n * node + 1 + c
				children.append((index,self.tree[index]))
			except IndexError:
				pass
			c += 1
		return children

	def getParent(self,node):
		try:
			index = int((node - 1) / self.n)
			if index < 0:
				return None
			else:
				return self.tree[index]
		except IndexError:
			return None

	def preOrder(self,index):
		print self.tree[index]
		for child in childrenHelper(self.getChildren(index),"index"):
			self.preOrder(child)

	def postOrder(self):
		pass

	def inOrder(self):
		pass

def parse(string):
	item = ""
	items = []
	for char in string:
		if char == " ":
			items.append(item)
			item = ""
		else: 
			item += char
	items.append(item)
	return items

def childrenHelper(tuples,info):
	children = []
	for tup in tuples:
		if info == "data":
			children.append(tup[1])
		elif info == "index":
			children.append(tup[0])
	return children

def main():
	#todo ask user if they need to sort their tree data first, read in data from file
	nodes = parse(raw_input("Enter the nodes of the tree, separated by spaces: "))
	n = input("Enter the maximum number of children per node: ")
	print "creating tree..."
	tree = Tree(nodes,n)
	for index, node in enumerate(tree.tree):
		print "Node: ",node, "Children: ", ",".join(childrenHelper(tree.getChildren(index),"data")), "Parent: ", tree.getParent(index) 
	print "preorder:"
	tree.preOrder(0)

if __name__=="__main__":
	main()
