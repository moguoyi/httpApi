from math import sqrt
# class Secretive:
#
#     def __inaccessible(self):
#      print("这事一个私有方法")
#
#     def accessible(self):
#         print("这是一个就可以引用私有方法的共有类方式:")
#         self.__inaccessible()
#
# # s=Secretive()
# # s._Secretive__inaccessible()
#
# class Calculator:
#     def calculate(self,expresssion):
#         self.value=eval(expresssion)
#
# class Talker:
#     def talker(self):
#         print('my name is {}'.format(self.value))
#
# class TalkerCalculator(Calculator,Talker):
#     pass
#
# # tc=TalkerCalculator()
# # tc.calculate('1+3+87')
# # tc.talker()
# try:
#     x=int(input('Enter the first number: '))
#     y=int(input('Enter the second number: '))
#     print(x/y)
# except ZeroDivisionError:
#     print("The second number can't be zero!")
# x=1
# while x<=100:
#     print(x)
#     x+=1
# for n in range(99,0,-1):
#     root=sqrt(n)
#     print(root,n)
#     if root==int(root):
#         print(n)
#         break


def mo():
    x=int(input("请输出汉字字符："))
    while True:
     if int(x)<=0:
        x=int(input("请输出汉字字符:"))
        continue
     else:
        # print(x)
        return x
        break
y=mo()
print(y)