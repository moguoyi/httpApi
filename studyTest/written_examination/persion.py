#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020-08-12 20:17
# @Author  : moguoyi
# @Email   : moguoyi@163.com
# @File    : persion.py
# @Software: PyCharm


class Persion:
    x = 5
    y = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y


person = Persion(10, 20)
person.z = 7
print(person.x)
print(person.y)
print(Persion.x)
print(Persion.y)
print(Persion.add(Persion))
print(person.add())
print(Persion.z)
print(person.z)