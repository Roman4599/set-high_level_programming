#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_creation(self):
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_str(self):
        self.assertEqual(str(Square(5, 2, 3, 10)), "[Square] (10) 2/3 - 5")

    def test_update(self):
        s = Square(5)
        s.update(99, 10, 1, 2)
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 10)
        s.update(x=5)
        self.assertEqual(s.x, 5)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.to_dictionary(), {'id': 10, 'size': 5, 'x': 2, 'y': 3})
        