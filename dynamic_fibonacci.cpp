#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

int fib(int n, int memo[]) {
	bool exists = find(begin(memo), end(memo), n) != end(memo);
	if (exists) {
		return memo[n];
	}
	else {
		int f = fib(n-1,memo) + fib(n-2,memo);
	}
	memo[n] = f;
	return f;
	}

int main():
	int n;
	int memo [n];
	cout << "How many terms?";
	cin >> n;
	num = fib(n,memo);
	cout << num;
	return 0;

