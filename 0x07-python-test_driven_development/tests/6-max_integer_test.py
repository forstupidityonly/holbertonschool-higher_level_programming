#!/usr/bin/python3
"""max integer module"""
import unittest
max_integer = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
     """for max_integer"""
     def test_man(self):
          self.assertEqual(max_integer([1, 2, 3]), 3)
          self.assertEqual(max_integer([9, 23, 4]), 23)
          self.assertEqual(max_integer([-3, -23, -4]), -3)
          self.assertEqual(max_integer([34]), 34)
          self.assertIsNone(max_integer())
