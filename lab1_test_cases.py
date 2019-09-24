import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([3]), 3)
        self.assertEqual(max_list_iter([4, 2, 3]), 4)
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([]), None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(8, 0, 2, []), None)
        self.assertEqual(bin_search(9, 0, len(list_val) - 1, list_val), 7)
        self.assertEqual(bin_search(11, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(4, 2, 2, list_val), None)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)


if __name__ == "__main__":
        unittest.main()