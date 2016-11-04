#!/usr/bin/env python2

class Solution:

    memo = {}

    def fibonacci(self, n):
        if n in self.memo.keys(): return self.memo[n]
        if n <= 2: f = 1
        else: f = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.memo[n] = f
        return f

def main():
	n = input("Number of terms to compute: ")
	val = fib(n)
	print "__\n", val
	print "Number of digits:", len(str(val))

if __name__=="__main__":
	memo = {}
	main()

