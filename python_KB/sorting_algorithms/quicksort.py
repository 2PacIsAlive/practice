#!usr/bin/env python

import random

def randomizeString(string):
	new = []
	old = list(enumerate(string))
	while old != []:
		new.append(old.pop(random.randint(0,len(old)-1)))
	return new

def partition(array,low,high):
	pivot = array[high]
	swap = low
	for i in range(low,high):
		if array[i][0] <= pivot[0]:
			tmp = array[swap]
			array[swap] = array[i] 
			array[i] = tmp
			swap += 1
	tmp = array[swap]
	array[swap] = array[high]
	array[high] = tmp
	return swap

def quickSort(array,low,high):
	if low < high:
		p = partition(array,low,high)
		quickSort(array, low, p-1)
		quickSort(array, p+1, high)

def main():
	string = raw_input("Enter a string: ")	
	random_string = randomizeString(string)
	print "\n"
	print "Randomized string: "
	for val, char in random_string:
		print char,
	print "\n"
	sorted_string = random_string #operate on global list
	quickSort(sorted_string,0,len(string)-1)
	print "Sorted string: "
	for val, char in sorted_string:
		print char, 

if __name__=="__main__":
	sorted_string = []
	main()
