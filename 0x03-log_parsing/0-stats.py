#!/usr/bin/python3

import sys


def print_statistics(status_codes, total_file_size):
    """
    Print statistics.
    
    Args:
        status_codes (dict): Dictionary of status codes and their counts.
        total_file_size (int): Total file size.
    """
    print("Total File Size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("Status Code {}: {}".format(code, count))


def main():
    total_file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            if line_count > 10:
                break

            parts = line.split()
            if len(parts) >= 2:
                total_file_size += int(parts[-2])  # Assuming file size is before status code
                status_code = parts[-1]  # Assuming status code is the last element
                if status_code in status_codes:
                    status_codes[status_code] += 1

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    finally:
        print_statistics(status_codes, total_file_size)


if __name__ == "__main__":
    main()

