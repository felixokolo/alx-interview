#!/usr/bin/python3
"""
Statistics calculation
"""
import sys
import re

stdin = sys.stdin
rex = (r'^([0-9]{1,3}\.){3}\d{1,3}\s-\s\[\d{4}' +
       r'-[0-1][0-2]-[0-3]\d\s[0-2][0-9]:([0-5]' +
       r'[0-9]:?){2}\.\d*\]\s"GET \/projects\/260 ' +
       r'HTTP\/1\.1"\s\d{3}\s\d+$')
rex2 = r'\d{3}\s\d+$'
status_codes = {200: 0, 301: 0,
                400: 0, 401: 0,
                403: 0, 404: 0,
                405: 0, 500: 0
                }
total_size = 0
loops = 0


try:
    for line in stdin:
        found = re.search(rex, line)
        if found is not None:
            code_size = re.search(rex2, found.string)
            code, size = found.string[code_size.start():].strip().split(' ')
            if int(code) in status_codes:
                status_codes[int(code)] += 1
                total_size += int(size)
                loops += 1
        if loops == 10:
            print('File size: {}'.format(total_size))
            sorted_keys = list(status_codes.keys())
            sorted_keys.sort()
            for k in sorted_keys:
                if status_codes[k] > 0:
                    print('{}: {:d}'.format(k, status_codes[k]))
            loops = 0
    print('File size: {}'.format(total_size))
    sorted_keys = list(status_codes.keys())
    sorted_keys.sort()
    for k in sorted_keys:
        if status_codes[k] > 0:
            print('{}: {:d}'.format(k, status_codes[k]))
except(KeyboardInterrupt):
    to_print = 'File size: {:d}\n'.format(total_size)
    sorted_keys = list(status_codes.keys())
    sorted_keys.sort()
    for k in sorted_keys:
        if status_codes[k] > 0:
            to_print += '{}: {:d}\n'.format(k, status_codes[k])
    print(to_print, end='')
    raise
