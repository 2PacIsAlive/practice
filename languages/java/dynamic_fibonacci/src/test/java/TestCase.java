import java.util.List;
import java.util.Arrays;

import org.junit.Test;
import static org.junit.Assert.*;

public class TestCase {
    @Test public void testComputingTheFirstTenTerms() {
        Solution solution = new Solution();
        List<Integer> answers = Arrays.asList(1, 1, 1, 2, 3, 5, 8, 13, 21, 34);
        for (int n=0; n<10; n++) {
            Integer correct = answers.get(n);
            Integer guess = solution.fibonacci(n);
            assertEquals("fibonacci(" + Integer.toString(n) + ") should return " + Integer.toString(correct), correct, guess);
        }
    }
}
