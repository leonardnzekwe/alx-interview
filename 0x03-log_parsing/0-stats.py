#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

from sys import stdin

status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0


def print_statistics():
    """Prints computed statistics"""
    print("File size:", total_file_size)
    for key, value in status_dict.items():
        if value:
            print("{}: {}".format(key, value))


def parse_line(line):
    """Parses a line and updates metrics"""
    global total_file_size, line_count

    line_count += 1
    parts = line.split()

    try:
        file_size = int(parts[-1])
        total_file_size += file_size
    except (IndexError, ValueError, TypeError):
        return

    try:
        status_code = int(parts[-2])
        if status_code in status_dict:
            status_dict[status_code] += 1
    except (IndexError, ValueError, TypeError):
        return

    if line_count == 10:
        print_statistics()
        line_count = 0


try:
    for line in stdin:
        parse_line(line.strip())

    print_statistics()

except KeyboardInterrupt:
    print_statistics()
