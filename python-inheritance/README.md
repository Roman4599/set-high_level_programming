# Python - Inheritance

Python project on object inheritance.

## Files

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | Returns the list of available attributes and methods of an object. |
| `1-my_list.py` | `MyList` class inheriting from `list`, with a `print_sorted()` method. |
| `tests/1-my_list.txt` | Doctests for `1-my_list.py`. |
| `2-is_same_class.py` | Returns True if the object is exactly an instance of the specified class. |
| `3-is_kind_of_class.py` | Returns True if the object is an instance of, or inherited from, the specified class. |
| `4-inherits_from.py` | Returns True if the object is an instance of a class that inherited from the specified class. |
| `5-base_geometry.py` | Empty `BaseGeometry` class. |
| `6-base_geometry.py` | `BaseGeometry` class with an `area()` method that raises an `Exception`. |
| `7-base_geometry.py` | `BaseGeometry` with `area()` and `integer_validator()` methods. |
| `tests/7-base_geometry.txt` | Doctests for `7-base_geometry.py`. |
| `8-rectangle.py` | `Rectangle` class inheriting from `BaseGeometry` with validated private width and height. |
| `9-rectangle.py` | `Rectangle` with `area()` and `[Rectangle] <width>/<height>` string representation. |
| `10-square.py` | `Square` class inheriting from `Rectangle`, printing as a rectangle. |
| `11-square.py` | `Square` printing as `[Square] <size>/<size>`. |
| `100-my_int.py` | `MyInt` class inheriting from `int`, with inverted `==` and `!=` operators. |
| `101-add_attribute.py` | Adds a new attribute to an object if possible. |

## Requirements

- Ubuntu 20.04 LTS
- python3 (version 3.8.5)
- Python code follows PEP 8 style (`pycodestyle`)
