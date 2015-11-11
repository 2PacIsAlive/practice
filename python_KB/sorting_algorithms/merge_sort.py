#!usr/bin/env python

import random

def randomizeString(string):#this function can use random.shuffle(string) instead...
	rand = []
	sortme = list(enumerate(string))
	while sortme != []:
		i = random.randint(0,len(sortme)-1)
		rand.append(sortme.pop(i))
	return rand

def mergeSort(arr):
	if len(arr) <= 1:
		return arr
	left = []
	right = []
	middle = len(arr)/2
	end = len(arr)
	#print "left"
	for x in range(0,middle):
		left.append(arr[x])
	#print left
	#print "right"
	for y in range(middle,end):
		right.append(arr[y])
	#print right
	left = mergeSort(left)
	right = mergeSort(right)
	return merge(left,right)	 	 

def merge(left,right):
	result = []
	while left != [] and right != []:
		#print "left",left
		#print "right",right
		if left[0][0] <= right[0][0]:
			result.append(left[0])
			left.pop(0)
		else:
			result.append(right[0])
			right.pop(0)
	while left != []:
		result.append(left[0])
		left.pop(0)
	while right != []:
		result.append(right[0])
		right.pop(0)
	return result	

def main():
	string = raw_input("Enter a string: ")
	random_string = randomizeString(string)
	print "Randomized string:"
	for val, char in random_string:
		print char,
	print
	print "Sorted string:"
	sorted_string = mergeSort(random_string)
	for val, char in sorted_string:
		print char,

if __name__=="__main__":
	main()
