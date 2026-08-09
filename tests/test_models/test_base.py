#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_ids(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{"id": 1, "width": 10}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 1, "width": 10}]')

    def test_save_to_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')
        os.remove("Rectangle.json")

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        s = '[{"id": 1, "width": 10}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 1, "width": 10}])

    def test_create(self):
        r = Rectangle.create(id=7, width=10, height=3, x=1, y=2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 10)

    def test_load_from_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        os.remove("Rectangle.json")

    def test_csv(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), r.to_dictionary())
        os.remove("Rectangle.csv")