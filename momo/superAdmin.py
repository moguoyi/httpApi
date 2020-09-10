#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class Other(object):

    def override(self):
        print("这里是other的override")

    def implicit(self):
        print("这里是other的implicit")

    def altered(self):
        print("这里是orher的altered")

class Child(object):

    def __init__(self):
        self.other=Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        # self.other.override()
        print("这里是Child的override")

    def altered(self):
        print("这里是child的altered")
        self.other.altered()
        print("这里是child和other的")

son=Child()

son.implicit()
son.override()
son.altered()
