import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 3]), 3)  # testing result last in list
        self.assertEqual(max_list_iter([3]), 3)  # testing list with 1 value
        self.assertEqual(max_list_iter([4, 2, 3]), 4)  # testing result first in list
        self.assertEqual(max_list_iter([-4, -2, -3]), -2)  # testing result middle of list and negatives
        self.assertEqual(max_list_iter([]), None)  # testing empty list

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)
            # used to check for exception
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # testing
        self.assertEqual(reverse_rec([1]), [1])  # testing list with 1 value
        self.assertEqual(reverse_rec([]), None)  # testing empty list

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)
            # used to check for exception
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)  # testing target in middle of list
        self.assertEqual(bin_search(8, 0, 2, []), None)  # testing value out of range but in list
        self.assertEqual(bin_search(9, 0, len(list_val) - 1, list_val), 7)  # testing
        self.assertEqual(bin_search(11, 0, len(list_val) - 1, list_val), None)  # testing value not in list
        self.assertEqual(bin_search(4, 2, 2, list_val), None)  # testing range of 0
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)  # testing value at end of list
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)  # testing value at beginning of list


if __name__ == "__main__":
        unittest.main()