#!/usr/bin/python3
"""
Statistics calculation
"""
import sys


def printStatus(status_codes, total_size):
    """ Prints information """
    print('File size: {:d}'.format(total_size))
    sorted_keys = sorted(status_codes.keys())
    for k in sorted_keys:
        if status_codes[k] > 0:
            print('{}: {:d}'.format(k, status_codes[k]))


stdin = sys.stdin
status_codes = {'200': 0, '301': 0,
                '400': 0, '401': 0,
                '403': 0, '404': 0,
                '405': 0, '500': 0
                }
total_size = 0
loops = 0

try:
    for line in stdin:
        if loops == 10:
            printStatus(status_codes, total_size)
            loops = 0
        loops += 1
        code = 0
        size = 0
        found = line.split(' ')
        try:
            if found[-1].strip().isnumeric():
                size = int(found[-1])
                total_size += size
        except(Exception):
            pass
        try:
            if found[-2].isnumeric():
                code = found[-2]
            if code in status_codes:
                status_codes[code] += 1
        except(Exception):
            pass
except(KeyboardInterrupt):
    printStatus(status_codes, total_size)
    raise
