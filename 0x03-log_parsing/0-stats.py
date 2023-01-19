#!/usr/bin/python3
"""
Statistics calculation
"""
import sys
import re

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

for line in sys.stdin:
    found = re.search(rex, line)
    if found is not None:
        code_size = re.search(rex2, found.string)
        code, size = found.string[code_size.start():].strip().split(' ')
        status_codes[int(code)] += 1
        total_size += int(size)
    loops += 1
    if loops == 10:
        print('File size:', total_size)
        for k, v in status_codes.items():
            print(f'{k}: {v}')
        loops = 0
    else:
        pass
