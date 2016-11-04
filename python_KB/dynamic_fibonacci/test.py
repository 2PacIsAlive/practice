import unittest

from dynamic_fibonacci import Solution

class TestDynamicFibonacci(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.solution = Solution()

    def testComputingTheFirstTenTerms(self):
        correct_sequence = zip(
            [n for n in range(10)], 
            [1, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        )
        for n, term in correct_sequence:
            self.assertEqual(self.solution.fibonacci(n), term)

def runTests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDynamicFibonacci)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__': runTests()

