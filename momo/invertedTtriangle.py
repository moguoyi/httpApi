#!/usr/bin/env python3
row =int(input("Enter the number of row:"))
n=0
while n<=row:
     x=" "*n+"*"*(row-n)
     print(x)
     n+=1
