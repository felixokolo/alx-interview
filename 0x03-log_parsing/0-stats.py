#!/usr/bin/python3
"""
Statistics calculation
"""
import sys

def printStatus(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))

stdin = sys.stdin
status_codes = {200: 0, 301: 0,
                400: 0, 401: 0,
                403: 0, 404: 0,
                405: 0, 500: 0
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
        if found is not None:
            if found[-1].strip().isnumeric():
                size = int(found[-1])
                total_size += size
            if found[-2].isnumeric():
                code = int(found[-2])
            if code in status_codes:
                status_codes[code] += 1
except(KeyboardInterrupt, Exception):
    printStatus(status_codes, total_size)
    raise
