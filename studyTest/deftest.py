__metaclass__=type

class Person:

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello World! i'm %s." % self.name)

foo=Person()
foo.setName('mo')
foo.greet()