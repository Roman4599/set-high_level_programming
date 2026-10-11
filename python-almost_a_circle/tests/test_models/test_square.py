#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test the Square class."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle_subclass(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_is_base_subclass(self):
        self.assertIsInstance(Square(1), Base)

    def test_creation(self):
        square = Square(5, 2, 3, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_defaults(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_auto_id(self):
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)

    def test_size_setter(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_size_type(self):
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "9"

    def test_size_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -1

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        self.assertEqual(str(Square(5, 2, 3, 10)), "[Square] (10) 2/3 - 5")

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

    def test_display(self):
        square = Square(2)
        out = StringIO()
        with redirect_stdout(out):
            square.display()
        self.assertEqual(out.getvalue(), "##\n##\n")

    def test_display_with_offsets(self):
        square = Square(2, 1, 1)
        out = StringIO()
        with redirect_stdout(out):
            square.display()
        self.assertEqual(out.getvalue(), "\n ##\n ##\n")

    def test_update_all_args(self):
        square = Square(5)
        square.update(99, 10, 1, 2)
        self.assertEqual(square.id, 99)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_partial_args(self):
        square = Square(5)
        square.update(99, 10)
        self.assertEqual(square.id, 99)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 0)

    def test_update_extra_args_ignored(self):
        square = Square(5)
        square.update(99, 10, 1, 2, 3, 4)
        self.assertEqual(square.y, 2)

    def test_update_kwargs(self):
        square = Square(5)
        square.update(x=5)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.size, 5)

    def test_update_mixed_kwargs(self):
        square = Square(5)
        square.update(size=8, y=3)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.y, 3)

    def test_update_no_args(self):
        square = Square(5, 2, 3, 10)
        square.update()
        self.assertEqual(square.to_dictionary(),
                         {'id': 10, 'size': 5, 'x': 2, 'y': 3})

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 10)
        self.assertEqual(square.to_dictionary(),
                         {'id': 10, 'size': 5, 'x': 2, 'y': 3})

    def test_to_dictionary_returns_dict(self):
        self.assertIsInstance(Square(1).to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
