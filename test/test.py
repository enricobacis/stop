#!/usr/bin/env python

from random import gauss
from time import sleep

try:
    while True:
        print int(gauss(100, 50))
        sleep(.0001)

except KeyboardInterrupt:
    pass

