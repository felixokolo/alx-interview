#!/usr/bin/python3
"""
Statistics calculation
"""
import sys

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
            print('File size: {}'.format(total_size))
            sorted_keys = list(status_codes.keys())
            sorted_keys.sort()
            for k in sorted_keys:
                if status_codes[k] > 0:
                    print('{}: {}'.format(k, status_codes[k]))
            loops = 0
        loops += 1
        code = 0
        size = 0
        found = line.split(' ')
        """ if len(fouprint('File size: {}'.format(total_size))nd[0]) < 4:
            continue
        if found[1] != '-':
            continue
        if found[2][0] != '[' or found[3][-1] != ']':
            continue
        if found[4] != '"GET':
            continue
        if found[5] != '/projects/260':
            continue
        if found[6] != 'HTTP/1.1"':
            continue """
        if found is not None:
            if found[-1].strip().isnumeric():
                size = int(found[-1])
                total_size += size
            else:
                continue
            if found[-2].isnumeric():
                code = int(found[-2])
            else:
                continue
            if code in status_codes:
                status_codes[code] += 1
except(KeyboardInterrupt):
    print('File size: {}'.format(total_size))
    sorted_keys = list(status_codes.keys())
    sorted_keys.sort()
    for k in sorted_keys:
        if status_codes[k] > 0:
            print('{}: {}'.format(k, status_codes[k]))
    raise
