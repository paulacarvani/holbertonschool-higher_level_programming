#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test Cases"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertIsNone(max_integer([]),)
        self.assertEqual(max_integer([-6584789410681, 1]), 1)
        self.assertEquals(max_integer([]), None)
        self.assertEquals(max_integer([0, 0, 0]), 0)
        self.assertEquals(max_integer([0, 0, 1]), 1)

    def test_wrong_type(self):
        """Test Cases when Raises"""
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Paula", 1, 2, 4, -3])

if __name__ == '__main__':
    unittest.main()