#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


class Phone:
    """一个简单的类实例"""
    phoneColor = "经典黑"

    def f(self):
        return 'hello'


# 实例化类
x = Phone()

# 访问类的属性和方法
print("Phone 类的属性 phoneColor 为：%s" % x.phoneColor)
print("Phone 类的方法 f 输出为： %s" % x.f())
print("Phone类的对象 x 所有的属性和方法： %s" % x.__dir__())