#coding:utf-8

class One(object):

    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.m=self.foo()
    def foo(self):
        a=self.name
        b=a+self.id
        return b

if __name__=='__main__':
    mo=One(1,0)
    print(mo.m)
