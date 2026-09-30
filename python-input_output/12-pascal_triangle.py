#!/usr/bin/python3
"""Contains the pascal_triangle function."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists of integers."""
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        previous = triangle[-1]
        row = [1]
        for i in range(1, len(previous)):
            row.append(previous[i - 1] + previous[i])
        row.append(1)
        triangle.append(row)
    return triangle
