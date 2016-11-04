import java.util.HashMap;

public class Solution {

    HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();
    int answer;

    public Solution() {
        memo = new HashMap();
    }

    public int fibonacci(int n) {
        if (memo.containsKey(n)) { 
            return memo.get(n); 
        } else if (n <= 2) { 
            answer = 1;
        } else { 
            answer = fibonacci(n-1) + fibonacci(n-2); 
        }
        memo.put(n, answer);
        return answer;
    }
}
