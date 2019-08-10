#!/usr/bin/env python3
import math
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
d=b*b-4*a*c
if d<0:
  print("无解")
else:
 root1 = (-b + math.sqrt(d)) / (2*a)
 root2 = (-b - math.sqrt(d)) / (2*a)
print("值1="+root1)
print("值2="+root2)
