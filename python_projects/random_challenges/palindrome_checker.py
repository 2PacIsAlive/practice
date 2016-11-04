#!usr/bin/env python

import itertools

def checkPalindrome(word):
	if len(word) < 2:
		return 
	if word[0] != word[-1]:
		return False
	return checkPalindrome(word[1:-1])

def loadWords(file_):
	words = []
	file_ = open(file_)
	for word in file_:
		words.append(word[:-2])
	file_.close()
	return words

def main():
	data = loadWords("assets/lowercase.txt")
	for word in data:
		print word
		permutations = list(map("".join, itertools.permutations(word)))
		for combo in permutations:
			if checkPalindrome(combo) == None: 
				print combo, "is a palindrome!", "ROOT WORD:", word
		else:
			#print word, "is not a palindrome."
			pass

if __name__=="__main__":
	main()
