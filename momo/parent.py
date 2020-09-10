#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

class Parent(object):

    def override(self):
        print("这里是父类的override")

    def implicit(self):
        print("这里是父类的implicit方法")

    def altered(self):
        print("这里是父类的altered")


class Child(Parent):
    # print("这里是子类")
    # pass
    def override(self):
        print("这里是子类的overried")

    # def implicit(self):
    #     print("这里是子类的方法")
    #     super(Child,self).implicit()
    #     print("子类父类")
    #     # Parent.implicit(self)
    def altered(self):
        print("这里是子类的父类1")
        # super(Child,self).altered()
        super().altered()
        print("子类的父类2")

dad=Parent()
son=Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()