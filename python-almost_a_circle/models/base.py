#!/usr/bin/python3
"""Base class for all models."""
import json
import turtle


class Base:
    """Manages the id attribute and shared serialization helpers."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): If provided, assigned to the instance; otherwise an
                auto-incremented id is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries to serialize.

        Returns:
            str: the JSON representation, or "[]" when the list is empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of instances to a file.

        Args:
            list_objs (list): list of instances inheriting from Base.
        """
        filename = cls.__name__ + ".json"
        data = []
        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): the JSON string to parse.

        Returns:
            list: the parsed list, or an empty list if json_string is empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set.

        Args:
            **dictionary: keyword arguments matching the attribute names.

        Returns:
            Base: an instance of the calling class with the given attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file.

        Returns:
            list: the list of instances, or an empty list if the file is
                missing.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                content = file.read()
        except IOError:
            return []
        list_dicts = cls.from_json_string(content)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of a list of instances to a file.

        Args:
            list_objs (list): list of instances inheriting from Base.
        """
        filename = cls.__name__ + ".csv"
        rows = []
        if list_objs is not None:
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    rows.append("{},{},{},{},{}".format(
                        obj.id, obj.width, obj.height, obj.x, obj.y))
                else:
                    rows.append("{},{},{},{}".format(
                        obj.id, obj.size, obj.x, obj.y))
        with open(filename, "w") as file:
            for row in rows:
                file.write(row + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from a CSV file.

        Returns:
            list: the list of instances, or an empty list if the file is
                missing.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                content = file.read()
        except IOError:
            return []
        instances = []
        for line in content.splitlines():
            if not line.strip():
                continue
            values = [int(value) for value in line.split(",")]
            if cls.__name__ == "Rectangle":
                dictionary = {
                    "id": values[0], "width": values[1],
                    "height": values[2], "x": values[3], "y": values[4]
                }
            else:
                dictionary = {
                    "id": values[0], "size": values[1],
                    "x": values[2], "y": values[3]
                }
            instances.append(cls.create(**dictionary))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all Rectangles and Squares.

        Args:
            list_rectangles (list): list of Rectangle instances to draw.
            list_squares (list): list of Square instances to draw.
        """
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()
        turtle.title("Almost a Circle")
        turtle.bgcolor("black")

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.setheading(0)
            pen.pendown()
            pen.color("cyan", "blue")
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.end_fill()

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.setheading(0)
            pen.pendown()
            pen.color("yellow", "red")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        turtle.done()
