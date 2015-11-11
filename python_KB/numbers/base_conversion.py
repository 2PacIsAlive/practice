#!usr/bin/env python

def reverse(numList):
	num = ''
	while numList != []:
		num += str(numList.pop())
	return int(num) 

def convert(num, base):
	newnum = []
	while num != 0:
		remainder = num % base
		newnum.append(remainder)
		num = num // base
	return reverse(newnum)

def main():
	random_num = input("Enter a base 10 number: ")
	base = input("Enter new base: ")
	print "Converting", random_num, "from base 10 to base", base
	new_num = convert(random_num,base)
	print new_num

if __name__=="__main__":
	main()
