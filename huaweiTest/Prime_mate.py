#coding:utf-8
# import sys
# n=int(input())
# while True:
#     for i in range(n):
#         num=sys.stdin.readline().strip()
#     break
# while True:
     # num=int(input("请输入一个数："))
# num=15
# for i in range(2,num):
#   if(num%i==0):
#        print("%d不为素数"%num)
#        break
# else:
#   print("%d是素数"%num)

def mate(n):

        for i in range(2,n):
            if(n%i==0):
                return False
                break
        else:

                return True



print(mate(9))