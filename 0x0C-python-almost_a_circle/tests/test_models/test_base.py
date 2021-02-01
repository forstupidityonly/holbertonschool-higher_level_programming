#!/usr/bin/python3
"""[summary]
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """base class test"""
    def test_id(self):
        """do it id?"""
        self.assertEqual(base.id, 1)
