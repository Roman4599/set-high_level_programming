#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
