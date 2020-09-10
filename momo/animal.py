# --*-- coding:utf-8 --*--

class readfile(object):
    def da(self):
        pass

class mo(readfile):
    def da(self):
        print("yi")

class kk(readfile):
    def da(self):
        print("kk")

def func(obj):
    obj.da()

Mo=mo()
func(Mo)

