#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020-08-12 19:52
# @Author  : moguoyi
# @Email   : moguoyi@163.com
# @File    : copy_deepcopy.py
# @Software: PyCharm
import copy

a = ('1', '2', '3')
b = copy.copy(a)
c = copy.deepcopy(a)
print(b == c)
print(id(b) == id(c))
print(id(b), id(c))
print(b, c)


"""
元组结果一样:原因为不可变对象
list结果不一样 原因为可变对象
字典结果不一样：原因为可变对象
"""