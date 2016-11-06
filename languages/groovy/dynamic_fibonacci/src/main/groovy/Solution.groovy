class Solution {

    def memo = [:]
    int answer

    int fibonacci(n) {
        if (memo.containsKey(n)) {
            return memo.get(n)
        } else if (n <= 2) {
            answer = 1
        } else {
            answer = fibonacci(n-1) + fibonacci(n-2)
        }
        memo.put(n, answer)
        return answer
    }
}
