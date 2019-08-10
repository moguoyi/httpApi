#!/usr/bin/env python3
# -*- coding:UTF-8 -*_
n=int(input("请输入学生人数："))
subjects=('数学','物理','历史')
data={}
for i in range(0,n):
   name=input("请输入第{}个学生姓名：".format(i+1))
   mark=[]
   for j in subjects:
      mark.append(int(input("请输入{}分数：".format(j))))
   data[name]=mark
for x, y in data.items():
   total= sum(y)
   print("{}'s total marks {}".format(x,total))
   if total<120:
       print(x,"failed:(")
   else:
       print(x,"passed:)")
