#!usr/bin/env python:

import os
import ipdb
breakP = ipdb.set_trace

def UI():
	context = raw_input("What would you like to do? (hint: help) ")
	if context == "help":
		help_()
	elif context == "review":
		review_()
	elif context == "study":
		study_()
	elif context == "make":
		make_()
	elif context == "quit":
		return
	else:
		print "Unrecognized input"
	UI()
	
def help_():
	options = ["help, review, study, make, quit"]
	print "\nOPTIONS:"
	for option in options:
		print option

def review_():
	context = raw_input("What would you like to review? (hint: help) ")
	if context == "BFS and DFS":
		os.system("python graphs/BFS_DFS.py")
	else:
		print "Unrecognized input"

def study_():
	return

def make_():
	context = raw_input("What would you like to make? (hint: help) ")
	if context == "help":
		options = ["help","data","graph", "tree", "hashtable", "sorter"]
		print "\nOPTIONS:"
		for option in options:
			print option
	elif context == "data":
		filename = raw_input("Name of data file: ")
		data = raw_input("Enter data, separated by spaces: ")
		file_ = open(filename, "w")
		file_.write(data)
		file_.close()
		print "Data file", filename, "created." 
	elif context == "tree":
		type_ = raw_input("What kind of tree?")
		if type_ == "k-ary":
			os.system("python trees/k-ary.py")
		else:
			print "Unrecognized input"
	else:
		print "Unrecognized input"


def main():
	UI()
	print "Goodbye!"

if __name__=="__main__":
	main()
