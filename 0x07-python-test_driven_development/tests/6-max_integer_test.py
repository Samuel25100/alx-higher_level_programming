#!/usr/bin/python3
"""Unittest for max_integer from list."""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class of Unittest of max_integer."""

    def test_max_int(self):
        """Test using positive integer."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 4, 2, 3]), 4)

    def test_negative_int(self):
        """Test using negative integer."""
        self.assertEqual(max_integer([0, -1, -3, -5]), 0)
        self.assertEqual(max_integer([-2, -91, -31, -4]), -2)
        self.assertEqual(max_integer([-9, -14, 23, -9, -100, 0]), 23)

    def test_empty_list(self):
        """Test using empty list or None."""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer([None]), None)

    def test_one_arg(self):
        """Test on list with only one argument."""
        self.assertEqual(max_integer([26]), 26)


if __name__ == '__main__':
    unittest.main()
