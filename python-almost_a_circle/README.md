# Python - Almost a Circle

A Python package that models geometric shapes with a shared serialization
layer. The project explores Python's Object-Oriented Programming features:
inheritance, private attributes, properties, class/static methods, and
JSON/CSV serialization.

## Directory layout

```
python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py        # Base class (id, serialization, draw)
│   ├── rectangle.py   # Rectangle class (inherits from Base)
│   └── square.py      # Square class (inherits from Rectangle)
├── tests/
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_base.py
│       ├── test_rectangle.py
│       └── test_square.py
├── 0-main.py
└── README.md
```

## Classes

### Base

- `Base(id=None)`: manages the `id` attribute. When `id` is `None`, an
  auto-incremented integer is assigned.
- `to_json_string(list_dictionaries)`: returns the JSON string of a list of
  dictionaries (`"[]"` when the list is empty or `None`).
- `save_to_file(list_objs)`: writes the JSON representation to
  `<ClassName>.json`.
- `from_json_string(json_string)`: parses a JSON string into a list.
- `create(**dictionary)`: returns an instance built from a dictionary.
- `load_from_file()`: returns a list of instances loaded from
  `<ClassName>.json`.
- `save_to_file_csv(list_objs)` / `load_from_file_csv()`: the CSV variants.
- `draw(list_rectangles, list_squares)`: opens a Turtle window and draws
  every rectangle and square in different colors.

### Rectangle

- `Rectangle(width, height, x=0, y=0, id=None)`
- Properties with validation: `width`, `height` (integer `> 0`) and `x`,
  `y` (integer `>= 0`). Invalid types raise `TypeError`, invalid values
  raise `ValueError`.
- `area()`: returns `width * height`.
- `display()`: prints the rectangle with `#` respecting `x` and `y`.
- `__str__()`: `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.
- `update(*args, **kwargs)` and `to_dictionary()`.

### Square

- `Square(size, x=0, y=0, id=None)`
- `size` property (delegates to `width`/`height`), `__str__()`, `update()`
  and `to_dictionary()`.

## Usage

```
guillaume@ubuntu:~/python-almost_a_circle$ cat 0-main.py
#!/usr/bin/python3
from models.base import Base

b1 = Base()
print(b1.id)

b2 = Base(12)
print(b2.id)

b3 = Base()
print(b3.id)

guillaume@ubuntu:~/python-almost_a_circle$ ./0-main.py
1
12
2
guillaume@ubuntu:~/python-almost_a_circle$
```

## Drawing

```python
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10)]
    list_squares = [Square(35), Square(15, 70, 50)]

    Base.draw(list_rectangles, list_squares)
```

Turtle needs Tk (`sudo apt-get install python3-tk`). To display the window
outside a VM, enable X11 forwarding.

## Testing

All classes and methods are unit tested with the `unittest` framework:

```
guillaume@ubuntu:~/python-almost_a_circle$ python3 -m unittest discover tests
...........................................................................
...........................................................................
...........
----------------------------------------------------------------------
Ran 83 tests in 0.074s

OK
guillaume@ubuntu:~/python-almost_a_circle$
```

You can also run a single test module:

```
python3 -m unittest tests.test_models.test_rectangle
```

## Style

All files comply with PEP 8 (`python3 -m pycodestyle models tests`).

## Author

[Roman4599](https://github.com/Roman4599)
