#!/usr/bin/python3

import sys

def print_statistics(status_codes, total_file_size):
    """
    Function to print file size and status code statistics
    Args:
        status_codes: dictionary of status codes
        total_file_size: total size of files
    Returns:
        None
    """
    print("Total File Size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))

total_file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    line_counter = 0
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_file_size += int(parsed_line[0])
                status_code = parsed_line[1]

                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_counter == 10:
                print_statistics(status_codes, total_file_size)
                line_counter = 0

finally:
    print_statistics(status_codes, total_file_size)
