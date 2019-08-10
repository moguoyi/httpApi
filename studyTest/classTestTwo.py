class Phone(object):
    """一个简单的类实例"""

    def __init__(self,brand,size):
        self.brand = brand
        self.size = size

# 实例化类
x = Phone("MI","5寸")

# 访问类的属性和方法
print("类对象 brand：%s" % x.brand)
print("类对象 size ： %s" % x.size)
print("Phone类的对象对象 x 所有的属性和方法： %s" % x.__dir__())

