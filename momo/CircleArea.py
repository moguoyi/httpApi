#!/usr/bin/env python3
import math
r=float(input("请输入半径r:"))
s=math.pi*r*r
if r!=0:
 print("圆面积S= {:.10f}".format(s))
else:
 print("输入半径值不能为0")
