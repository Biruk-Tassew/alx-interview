#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0


def print_stats():
    """
    Function that prints stats about log
    """
    global total_size

    print('File size: {}'.format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        if status_codes[code] > 0:
            print('{}: {}'.format(code, status_codes[code]))


if __name__ == "__main__":
    count = 0
    try:
        """ Iterate over the standard input """
        for data in sys.stdin:
            try:
                parts = data.split(' ')
                """ If there is a status code """
                if parts[-2] in status_codes:
                    status_codes[parts[-2]] += 1
                """ If there is a length """
                total_size += int(parts[-1])
            except:
                pass
            """ Printing control """
            count += 1
            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        raise
    else:
        print_stats()
