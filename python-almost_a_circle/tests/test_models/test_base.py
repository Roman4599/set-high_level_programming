#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
import models.base as base_module
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

FILES = ("Rectangle.json", "Square.json", "Rectangle.csv", "Square.csv")


class TestBase(unittest.TestCase):
    """Test the Base class and its serialization helpers."""

    def setUp(self):
        """Reset the auto-increment counter before every test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove any files created by a test."""
        for name in FILES:
            if os.path.exists(name):
                os.remove(name)

    # --- id management ---
    def test_id_auto(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_id_explicit(self):
        self.assertEqual(Base(12).id, 12)

    def test_id_mixed(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(50).id, 50)
        self.assertEqual(Base().id, 2)

    def test_id_is_int(self):
        self.assertIsInstance(Base().id, int)

    # --- to_json_string ---
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        data = [{"id": 1, "width": 10}]
        self.assertEqual(
            Base.to_json_string(data), '[{"id": 1, "width": 10}]')

    def test_to_json_string_returns_str(self):
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)

    # --- from_json_string ---
    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        text = '[{"id": 1, "width": 10}]'
        self.assertEqual(Base.from_json_string(text),
                         [{"id": 1, "width": 10}])

    def test_from_json_string_returns_list(self):
        self.assertIsInstance(Base.from_json_string("[]"), list)

    # --- save_to_file / load_from_file ---
    def test_save_to_file_rectangle(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(),
                '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_square(self):
        square = Square(5, 2, 3, 10)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertEqual(
                file.read(), '[{"id": 10, "size": 5, "x": 2, "y": 3}]')

    def test_load_from_file_missing(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].to_dictionary(), rect.to_dictionary())

    def test_load_from_file_square(self):
        square = Square(3, 4, 5, 6)
        Square.save_to_file([square])
        loaded = Square.load_from_file()
        self.assertEqual(loaded[0].to_dictionary(), square.to_dictionary())

    # --- create ---
    def test_create_rectangle(self):
        rect = Rectangle.create(id=7, width=10, height=3, x=1, y=2)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.to_dictionary(),
                         {'id': 7, 'width': 10, 'height': 3, 'x': 1, 'y': 2})

    def test_create_square(self):
        square = Square.create(id=9, size=4, x=1, y=2)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.to_dictionary(),
                         {'id': 9, 'size': 4, 'x': 1, 'y': 2})

    def test_create_rectangle_partial(self):
        rect = Rectangle.create(width=7, height=8)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 0)

    # --- csv ---
    def test_csv_rectangle_roundtrip(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([rect])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), rect.to_dictionary())

    def test_csv_square_roundtrip(self):
        square = Square(3, 4, 5, 6)
        Square.save_to_file_csv([square])
        loaded = Square.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), square.to_dictionary())

    def test_csv_file_content(self):
        Rectangle.save_to_file_csv([Rectangle(1, 2, 3, 4, 5)])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "5,1,2,3,4\n")

    def test_load_from_file_csv_missing(self):
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    # --- draw ---
    def test_draw_is_staticmethod(self):
        self.assertIsInstance(Base.__dict__["draw"], staticmethod)

    def test_draw_runs(self):
        """draw() must iterate over both lists without real turtle calls."""
        class FakePen:
            def __getattr__(self, name):
                def noop(*args, **kwargs):
                    return None
                return noop

        class FakeTurtle:
            def Turtle(self):
                return FakePen()

            def __getattr__(self, name):
                def noop(*args, **kwargs):
                    return None
                return noop

        original = base_module.turtle
        base_module.turtle = FakeTurtle()
        try:
            Base.draw([Rectangle(2, 3), Rectangle(4, 5, 1, 1)], [Square(4)])
        finally:
            base_module.turtle = original


if __name__ == "__main__":
    unittest.main()
