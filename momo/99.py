#!/usr/bin/env python3
for i in range(1,10):
   for j in range(1,i+1):
       print("{}x{}\t".format(j,i*j),end="")
   print()
