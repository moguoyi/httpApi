#calc.py
class Calc:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b==0:
            return None
        else:
            return a/b

class Calc_Mock():

    def add(self, a, b):
        return (a+b)*2


if __name__=='__main__':
    mo=Calc_Mock()
    mo1=Calc()
    print(mo.add(2,2))
    print(mo1.add(1,1))