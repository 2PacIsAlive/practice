#!/usr/bin/python
import random
import ipdb
breakP = ipdb.set_trace

def makeRandomString(string):
	sortedList = list(enumerate(string))
	randomList = []	
	while sortedList != []:
		randomIndex = random.randrange(0,len(sortedList))
		randomList.append(sortedList.pop(randomIndex))
	return randomList

def insertionSort(unsortedList):
	for i in range(1,len(unsortedList)):
		key = unsortedList[i]
		j = i-1
		while (j >= 0 and unsortedList[j][0] > key[0]):
			unsortedList[j+1] = unsortedList[j]
			j = j-1
		unsortedList[j+1] = key
	return unsortedList

def main():
	string = "Take chances, make mistakes. That's how you grow. Pain nourishes your courage. You have to fail in order to practice being brave."
#	for i in range():
#		string += str(i)
	unsorted = makeRandomString(string)
	print "--------------------unsorted--------------------"
	for loc,val in unsorted:
		print val, 
	print
	sortedList = insertionSort(unsorted)
	print "---------------------sorted---------------------"
	output = []
	for loc,val in sortedList:
		output.append(val)
		#print val,
	for char in output:
		print char,
	
if __name__=="__main__":
	main()
