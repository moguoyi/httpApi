#!/usr/bin/env python3
import sys
def mo():
  times=sys.argv[1]
  time=int(times)
  if time<0:
       try:
         raise ValueError("Input number cannot be negative")
       except ValueError:
         print("Input number cannot be negative")
  else:
       hour=time//60
       minute=time%60
       print("{} H, {} M".format(hour,minute))
mo()
