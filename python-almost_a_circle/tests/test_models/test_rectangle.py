#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test the Rectangle class."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_is_base_subclass(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_defaults(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_full_creation(self):
        rect = Rectangle(5, 10, 1, 2, 99)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 99)

    def test_auto_id(self):
        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Rectangle(1, 1).id, 2)

    def test_width_setter(self):
        rect = Rectangle(1, 1)
        rect.width = 20
        self.assertEqual(rect.width, 20)

    def test_height_setter(self):
        rect = Rectangle(1, 1)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_setter(self):
        rect = Rectangle(1, 1)
        rect.x = 20
        self.assertEqual(rect.x, 20)

    def test_y_setter(self):
        rect = Rectangle(1, 1)
        rect.y = 20
        self.assertEqual(rect.y, 20)

    # --- type validation ---
    def test_width_type(self):
        with self.assertRaises(TypeError) as err:
            Rectangle("5", 10)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_height_type(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, "10")
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_x_type(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 10, "1")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_y_type(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 10, 1, "2")
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_width_type_float(self):
        with self.assertRaises(TypeError):
            Rectangle(5.5, 10)

    # --- value validation ---
    def test_width_value(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(-5, 10)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_height_value(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(5, -10)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_x_value(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(5, 10, -1)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_y_value(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(5, 10, 1, -2)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_validation_order(self):
        """width is checked before height."""
        with self.assertRaises(TypeError) as err:
            Rectangle("5", "10")
        self.assertEqual(str(err.exception), "width must be an integer")

    # --- area ---
    def test_area(self):
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_area_large(self):
        self.assertEqual(Rectangle(100, 40).area(), 4000)

    # --- __str__ ---
    def test_str(self):
        rect = Rectangle(4, 5, 1, 2, 99)
        self.assertEqual(str(rect), "[Rectangle] (99) 1/2 - 4/5")

    # --- display ---
    def test_display(self):
        rect = Rectangle(2, 2)
        out = StringIO()
        with redirect_stdout(out):
            rect.display()
        self.assertEqual(out.getvalue(), "##\n##\n")

    def test_display_with_x(self):
        rect = Rectangle(2, 2, 1)
        out = StringIO()
        with redirect_stdout(out):
            rect.display()
        self.assertEqual(out.getvalue(), " ##\n ##\n")

    def test_display_with_xy(self):
        rect = Rectangle(2, 2, 1, 1)
        out = StringIO()
        with redirect_stdout(out):
            rect.display()
        self.assertEqual(out.getvalue(), "\n ##\n ##\n")

    def test_display_with_y_only(self):
        rect = Rectangle(1, 2, 0, 2)
        out = StringIO()
        with redirect_stdout(out):
            rect.display()
        self.assertEqual(out.getvalue(), "\n\n#\n#\n")

    # --- update ---
    def test_update_all_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_update_partial_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 2)

    def test_update_extra_args_ignored(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50, 60)
        self.assertEqual(rect.y, 50)

    def test_update_kwargs(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(x=100, y=200)
        self.assertEqual(rect.x, 100)
        self.assertEqual(rect.y, 200)
        self.assertEqual(rect.width, 1)

    def test_update_mixed_kwargs(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=7, width=8)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)

    def test_update_no_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update()
        self.assertEqual(rect.to_dictionary(),
                         {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    # --- to_dictionary ---
    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(rect.to_dictionary(),
                         {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_to_dictionary_returns_dict(self):
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
