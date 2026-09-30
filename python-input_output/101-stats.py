#!/usr/bin/python3
"""Prints metrics computed from log lines read on standard input."""

import sys

STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]


def parse_line(line):
    """Return the status code and the file size held by a log line."""
    fields = line.split()
    return int(fields[-2]), int(fields[-1])


def print_stats(file_size, counts):
    """Print the total file size and the number of lines per status code."""
    print("File size: {}".format(file_size))
    for code in STATUS_CODES:
        if code in counts:
            print("{}: {}".format(code, counts[code]))


def main():
    """Read stdin, printing the metrics every 10 lines and when finished."""
    file_size = 0
    counts = {}
    lines = 0
    try:
        for line in sys.stdin:
            lines += 1
            code, size = parse_line(line)
            file_size += size
            if code in STATUS_CODES:
                counts[code] = counts.get(code, 0) + 1
            if lines % 10 == 0:
                print_stats(file_size, counts)
    finally:
        print_stats(file_size, counts)


if __name__ == "__main__":
    main()
