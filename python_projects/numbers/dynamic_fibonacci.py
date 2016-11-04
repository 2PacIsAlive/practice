#!usr/bin/env python

def fib(n):
	if n in memo.keys():
		return memo[n]
	if n <= 2:
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	memo[n] = f
	print f
	return f

def main():
	n = input("Number of terms to compute: ")
	val = fib(n)
	print "__\n", val
	print "Number of digits:", len(str(val))

if __name__=="__main__":
	memo = {}
	main()

