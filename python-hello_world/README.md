# Python - Hello, World

Python project on the basics: shell scripts, f-strings, string slicing and
one C task.

## Files

| File | Description |
| ---- | ----------- |
| `0-run` | Shell script running the Python file named by `$PYFILE`. |
| `1-run_inline` | Shell script running the Python code held by `$PYCODE`. |
| `2-print.py` | Prints a sentence using the `print` function. |
| `3-print_number.py` | Prints an integer followed by `Battery street` (f-string, 3 lines). |
| `4-print_float.py` | Prints a float with a precision of 2 digits (f-string). |
| `5-print_string.py` | Prints a string 3 times, then its first 9 characters. |
| `6-concat.py` | Concatenates two strings and greets the school (5 lines). |
| `7-edges.py` | Cuts a string into its first 3, last 2 and middle characters (8 lines). |
| `8-concat_edges.py` | Rebuilds a sentence from the edges of a string (5 lines). |
| `9-easter_egg.py` | Prints the title of `The Zen of Python` (max 98 characters). |
| `10-check_cycle.c` | C function checking if a singly linked list has a cycle. |
| `lists.h` | Header for the singly linked list task. |
| `10-linked_lists.c` | C helpers used to build and free the list under test. |
| `10-main.c` | Test harness for `check_cycle`. |
| `100-write.py` | Writes a quote to stderr with `sys.write` and exits with status 1. |
| `101-compile` | Shell script byte-compiling `$PYFILE` into `$PYFILEc`. |
| `102-magic_calculation.py` | Rebuilds a function from its Python bytecode. |

## check_cycle

`int check_cycle(listint_t *list)` returns `0` when the list has no cycle and
`1` when it has one. It uses Floyd's tortoise and hare: the slow pointer
advances one node while the fast one advances two, so a cycle shows up as both
pointers meeting. The list is left untouched and the algorithm runs in O(n)
time with O(1) extra space, using no function call at all.

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
./cycle
```

## Build and run

```bash
export PYFILE=main.py && ./0-run
export PYCODE='print(f"Best School: {88+10}")' && ./1-run_inline
./2-print.py
./3-print_number.py
./4-print_float.py
./5-print_string.py
./6-concat.py
./7-edges.py
./8-concat_edges.py
./9-easter_egg.py
./100-write.py 2> q
./101-compile
```

## Requirements

- Ubuntu 20.04 LTS
- python3 (version 3.8.5)
- C files compiled with `gcc -Wall -Werror -Wextra -pedantic -std=gnu89`
- Python code follows PEP 8 style (`pycodestyle`)
