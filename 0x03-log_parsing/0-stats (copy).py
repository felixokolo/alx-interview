#!/usr/bin/python3
"""
Statistics calculation
"""
import sys
import re

stdin = sys.stdin
rex = (r'^([0-9]{1,3}\.){3}\d{1,3}\s-\s\[\d{4}' +
       r'-[0-1][0-2]-[0-3]\d\s[0-2][0-4]:([0-5]' +
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

""" def handle(sign, frame):
    global pressed
    sys.stdout.flush()
    to_print = 'File size: {}\n'.format(total_size)
    sorted_keys = list(status_codes.keys())
    sorted_keys.sort()

    for k in sorted_keys:
        to_print += f'{k}: {status_codes[k]}\n'
        sys.stdout.write(to_print)

signal.signal(signal.SIGINT, handle) """

try:
    for line in stdin:
        found = re.search(rex, line)
        if found is not None:
            code_size = re.search(rex2, found.string)
            code, size = found.string[code_size.start():].strip().split(' ')
            status_codes[int(code)] += 1
            total_size += int(size)
        loops += 1
        if loops == 10:
            print('File size:', total_size)
            sorted_keys = list(status_codes.keys())
            sorted_keys.sort()
            for k in sorted_keys:
                print(f'{k}: {status_codes[k]}')
            loops = 0
except(KeyboardInterrupt):
    print('File size:', total_size)
    sorted_keys = list(status_codes.keys())
    sorted_keys.sort()
    for k in sorted_keys:
        print(f'{k}: {status_codes[k]}')
