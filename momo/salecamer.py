#!/usr/bin/env python3
a=200
b=0.02
z=1500
price=float(input("请输入售价："))
numbers=int(input("请输入数量："))
sales=(numbers*a+z*b*numbers)
print("一共获取的佣金  ={:2f}".format(sales))
