#!/usr/bin/env python2

import unittest

from Solution import Solution

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.solution = Solution()

    def testMethod(self):
        self.assertEqual(self.solution.method(), "correct_answer")

def runTests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__': runTests()
