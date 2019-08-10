class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):  # self=obj
        print('Foo.f2')  # 在父类中找到发 f2属性，第3步打印这一行
        self.f1()  # obj.f1()  第4步再去掉用self的f1属性


class Bar(Foo):
    def f1(self):  # 第五步， 在回到object自身的名称空间找f1属性，找到后调用
        print('Bar.f1')  # 第6步 执行


obj = Bar()  # 第一步 ：类的实例化， 先得到一个空对象，

obj.f2()  # 第2步：空对象调用f2属性 在自身寻找f2属性， 没有找到就去父类中寻找<br><br>#结果
