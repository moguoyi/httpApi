#!/usr/bin/env python3
#encoding:utf-8
import time
sentence = "I love you xiaoxiao"
for char in sentence.split():
   allChar = []
   for y in range(12, -12, -2):
       lst = []
       lst_con = ''
       for x in range(-100, 100):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   print('\n'.join(allChar))
   time.sleep(1)
