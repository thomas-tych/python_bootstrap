#!/usr/bin/env python3

def multiplication_table(num):
    "return string corresponding to NUM multiplication table"
    multiplication_table = ''
    for x in range(0, 11):
        multiplication_table += "%2d x %d = %2d\n" % (x, num, x * num)
    return multiplication_table

print(multiplication_table(7))

import time
time.sleep(10)
