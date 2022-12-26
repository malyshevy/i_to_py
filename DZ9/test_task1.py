import unittest
from task1 import split

class test_task1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testsimplestring(self):
        res = split([GOOG, 100, 490.50])
        self.assertEqual(res, ['GOOG', '100', '490.50'])

    def testtypeconvert(self):
        """test2"""
        res = split('GOOG 100 490.50', [str, int, float])
        self.assertEqual(res, ['GOOG', 100, 490.5])
