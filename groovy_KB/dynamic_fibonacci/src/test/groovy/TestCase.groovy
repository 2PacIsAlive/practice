import spock.lang.Specification

class TestCase extends Specification{
    def "computing the first ten terms"(int n, int answer) {
        setup:
        Solution solution = new Solution()
        expect:
        answer == solution.fibonacci(n)
        where:
        n | answer
        0 | 1
        1 | 1
        2 | 1
        3 | 2
        4 | 3
        5 | 5
        6 | 8
        7 | 13
        8 | 21
        9 | 34 
    }
}
