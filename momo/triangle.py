#!/usr/bin/env python3 
row=int(input("Enter the number of row:"))
n=1
while n<=row:
     x=' '*(n-1)+"*"*(row-n+1)
     y="*"*(row-n)+" "*(n-1)
     print(x+y)
     n+=1
