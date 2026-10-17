#!/usr/bin/python3
"""Solves the N queens puzzle."""

import sys


def solve_nqueens(n):
    """Return all solutions for placing N non-attacking queens."""
    solutions = []
    board = [0] * n

    def place(row):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            ok = True
            for prev in range(row):
                diff = col - board[prev]
                if diff == 0 or abs(diff) == row - prev:
                    ok = False
                    break
            if ok:
                board[row] = col
                place(row + 1)

    place(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in solve_nqueens(n):
        print(solution)
