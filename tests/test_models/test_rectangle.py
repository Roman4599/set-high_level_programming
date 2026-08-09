#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_creation(self):
        r = Rectangle(5, 10, 1, 2, 99)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 99)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            r = Rectangle("5", 10)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_area(self):
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/2 - 4/5")

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        expected = "\n ##\n ##\n"
        out = StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), expected)

    def test_update(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        r.update(x=100)
        self.assertEqual(r.x, 100)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        