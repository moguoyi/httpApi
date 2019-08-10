#!/usr/bin/env python3
str=input('请输入字符串：')
data=[]
for strs in str:
   if strs.isdigit():
      data.append(strs)
put=''.join(data)
print('输出的数字为：{}'.format(put))
