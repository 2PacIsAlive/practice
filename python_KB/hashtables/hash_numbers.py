#!usr/bin/env python

import random

class HashTable():
	def __init__(self, size):
		self.size = size
		self.buckets = [None] * self.size
		self.collisions = 0

	def hash_(self, data):
		return data % self.size

	def add_(self, number):
		hash_key = self.hash_(number)
		if self.buckets[hash_key] == None:
			self.buckets[hash_key] = number
		else: #collision
			self.collisions += 1
			stored = False
			while stored == False:
				if hash_key < self.size-1:
					hash_key += 1
				else: 
					hash_key = 0
				if self.buckets[hash_key] == None:
					self.buckets[hash_key] = number
					stored = True

	def find_(self,data):
		hash_key = self.hash_(data)
		if self.buckets[hash_key] == data:
			return self.buckets[hash_key]
		else:
			found = False
			while found == False:
				if hash_key < self.size-1:
					hash_key += 1
				else:
					hash_key = 0
				if self.buckets[hash_key] == data:
					found = True
					return self.buckets[hash_key]
			
def main():
	print "generating 100 random numbers..."
	data = random.sample(xrange(1000), 100)
	print "instantiating hash table..."
	hash_table = HashTable(len(data))
	print "adding data to hash table..."
	for number in data:
		hash_table.add_(number)
	print hash_table.collisions, "total collisions"
	print "finding data..."
	print "printing all buckets..."
	buckets = map(hash_table.find_,data)
	print buckets 

if __name__=="__main__":
	main()
