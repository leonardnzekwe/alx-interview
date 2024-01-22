#!/usr/bin/python3
"""Log Parsing Module"""
import sys


def print_statistics(total_size, status_codes):
    """Handles statistics printing"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line, total_size, status_codes):
    """parses stdin line"""
    try:
        parts = line.split(" ")
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_size += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_code not in status_codes:
                status_codes[status_code] = 0
            status_codes[status_code] += 1

    except (ValueError, IndexError):
        pass

    return total_size, status_codes


def main():
    """main program"""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_codes = parse_line(
                line.strip(), total_size, status_codes
            )

            if i % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:  # (CTRL + C)
        pass  # Allow KeyboardInterrupt to exit gracefully

    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
