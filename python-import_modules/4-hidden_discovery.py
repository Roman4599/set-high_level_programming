#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)
        code = marshal.load(f)
    names = []
    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            if not const.co_name.startswith("__"):
                names.append(const.co_name)
    for name in sorted(names):
        print(name)
