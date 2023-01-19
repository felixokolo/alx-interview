#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
    #^([0-9]{1,3}\.){3}\d{1,3}\s-\s\[\d{4}-[0-1][0-2]-[0-3]\d\s[0-2][0-4]:([0-5][0-9]:?){2}\.\d*\]\s"GET \/projects\/260 HTTP\/1\.1"(\s?\d{3}\s?){2}$