#!usr/bin/env python

class HashTable():
	def __init__(self): 
		self.size = 60000
		self.buckets = [None] * self.size
		self.current_hash = None
		self.num_collisions = 0
		
	def hash_(self,word):
		hash_value = abs(hash(word))
		hash_value = hash_value % self.size
		self.current_hash = hash_value
		return hash_value

	def rehash_(self,word):
		self.num_collisions += 1
		stored = False
		while stored == False:
			if self.current_hash < self.size-1:
				self.current_hash = self.current_hash+1
			else:
				self.current_hash = 0
			if self.buckets[self.current_hash] == None:
				stored = True
				return self.current_hash

	def loadData(self,filename):
		file_ = open(filename,"r")
		for word in file_:
			if self.buckets[self.hash_(word)] == None:
				self.buckets[self.hash_(word)] = word
			else:
				self.buckets[self.rehash_(word)] = word 	
	
def main():
	hash_table = HashTable()
	hash_table.loadData("assets/lowercase.txt")
	print hash_table.num_collisions

if __name__=="__main__":
	main()
