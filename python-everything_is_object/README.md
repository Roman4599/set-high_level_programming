# Python - Everything is object

Python project on object types, identifiers, mutability and CPython internals.

## Files

| File | Description |
| ---- | ----------- |
| `0-answer.txt` | Function to get the type of an object (`type`). |
| `1-answer.txt` | Function to get the variable identifier (`id`). |
| `2-answer.txt` | `a = 89` / `b = 100`: same object? |
| `3-answer.txt` | `a = 89` / `b = 89`: same object? |
| `4-answer.txt` | `a = 89` / `b = a`: same object? |
| `5-answer.txt` | `a = 89` / `b = a + 1`: same object? |
| `6-answer.txt` | `s2 = s1`, `s1 == s2` output. |
| `7-answer.txt` | `s2 = s1`, `s1 is s2` output. |
| `8-answer.txt` | Two equal string literals, `==` output. |
| `9-answer.txt` | Two equal string literals, `is` output. |
| `10-answer.txt` | Two equal list literals, `==` output. |
| `11-answer.txt` | Two equal list literals, `is` output. |
| `12-answer.txt` | `l2 = l1`, `==` output. |
| `13-answer.txt` | `l2 = l1`, `is` output. |
| `14-answer.txt` | `l1.append(4)` then `print(l2)`. |
| `15-answer.txt` | `l1 = l1 + [4]` then `print(l2)`. |
| `16-answer.txt` | Integer incrementation output. |
| `17-answer.txt` | List incrementation output. |
| `18-answer.txt` | List assignation output. |
| `19-copy_list.py` | Returns a copy of a list (3 lines). |
| `20-answer.txt` | `a = ()`: tuple? |
| `21-answer.txt` | `a = (1, 2)`: tuple? |
| `22-answer.txt` | `a = (1)`: tuple? |
| `23-answer.txt` | `a = (1, )`: tuple? |
| `24-answer.txt` | `a = (1)` / `b = (1)`, `a is b`. |
| `25-answer.txt` | `a = (1, 2)` / `b = (1, 2)`, `a is b`. |
| `26-answer.txt` | `a = ()` / `b = ()`, `a is b`. |
| `27-answer.txt` | `a = a + [5]` keeps the id? |
| `28-answer.txt` | `a += [4]` keeps the id? |
| `100-magic_string.py` | Returns `BestSchool` n times (4 lines). |
| `101-locked_class.py` | `LockedClass` forbidding dynamic attributes. |
| `103-line1.txt` | Int objects created by `a = 1` (line 1). |
| `103-line2.txt` | Int objects created by `b = 1` (line 2). |
| `104-line1.txt` | Int objects created by `a = 1024` (line 1). |
| `104-line2.txt` | Int objects created by `b = 1024` (line 2). |
| `104-line3.txt` | Is the int object of `a` deleted after line 3? |
| `104-line4.txt` | Is the int object of `b` deleted after line 4? |
| `104-line5.txt` | Int objects created by `c = 1024` (line 5). |
| `105-line1.txt` | Int objects still in memory before line 2. |
| `106-line1.txt` | String objects created by `a = "SCHL"` (line 1). |
| `106-line2.txt` | String objects created by `b = "SCHL"` (line 2). |
| `106-line3.txt` | Is the string object of `a` deleted after line 3? |
| `106-line4.txt` | Is the string object of `b` deleted after line 4? |
| `106-line5.txt` | String objects created by `c = "SCHL"` (line 5). |

## Requirements

- Ubuntu 20.04 LTS
- python3 (version 3.8.5)
- Python code follows PEP 8 style (`pycodestyle`)
- Answers assume a CPython implementation of Python 3 with default options