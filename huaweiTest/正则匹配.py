# !/usr/bin/env python
import re

while True:
    try:
        a = input().strip()
        b = input().strip()
        a = a.replace('*', '[1-9a-zA-Z]*').replace('?', '.')
        c = re.findall(a, b)
        c = ''.join(c)
        if c == b:
            print('true')
        else:
            print('fasle')
    except:
        break

