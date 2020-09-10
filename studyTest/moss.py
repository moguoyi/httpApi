#coding:utf-8
# str=input()
# print(str)
# str1=str.replace("\n",".")
# print(str1)
# listStr=str1.split(".")
# print(listStr)
# lineStr1=listStr[0]
# print(lineStr1)
# lineStr2=listStr[1]
# print(lineStr1.count(lineStr2))


# import  sys
# s=sys.stdin.readline()
# list=s.split()
# print(len(list[-1]))



# import sys
# while True:
#     try:
#         num=input()
#         num_list=[]
#         for i in range(num):
#             input_num=sys.stdin.readline()
#             num_list.append(int(input_num[:-1]))
#         num_list=sorted(list(set(num_list)))
#         for i in num_list:
#             print(i)
#     except:
#         break
# import sys
# first = sys.stdin.readline().strip("\n")
# second = sys.stdin.readline().strip("\n")
# list = []
# count = 0
# while count < len(first):
#     list.append(first[count:count+8])
#     count += 8
# # 对list[-1]进行补0处理
# if len(list[-1]) < 8:
#     list[-1] += '0'*(8-len(list[-1]))
# count = 0
# while count < len(second):
#     list.append(second[count:count+8])
#     count += 8
# if len(list[-1]) < 8:
#     list[-1] += '0'*(8-len(list[-1]))
# for j in list:
#     print (j)


import sys
# while True:
#     try:
#         s= sys.stdin.readline().strip("\n")
#         def count(s):
#             if len(s) <= 8:
#                 left = 8 - len(s)
#                 print(s + '0' * left)
#             else:
#                 print(s[:8])
#                 s = s[8:]
#                 count(s)
#         count(s)
    # except:
    #     break
# sys.exit()
# s= sys.stdin.readline().strip("\n")
# s1=sys.stdin.readline().strip("\n")
# def count(s):
#             if len(s) <= 8:
#                 left = 8 - len(s)
#                 print(s + '0' * left)
#             else:
#                 print(s[:8])
#                 s = s[8:]
#                 count(s)
# count(s)
# count(s1)


# def func():
#     x = input()
#     x = int('0x'+x, 16)
#     y = int(input())
#     str_out = ''
#     while True:
#         a = x // y
#         b = x % y
#         str_out += str(b)
#         if a == 0:
#             break
#         else:
#             x = a
#     print(str_out[::-1])
#
#
# if __name__ == '__main__':
#     func()

# import sys
#
# while True:
#     str=sys.stdin.readline().strip("\n")
#     try:
#         str=str.split("x")
#         str1=str[1]
#         print(int(str1,16))
#     except:
#         break

# def find_factors(number):
#     """
#     Print prime factors.
#     :param number: <int> number
#     :return: <None>
#     """
#
#  # 初始化is_prime变量为True，表示是质数
#     is_prime = True
#      # 查找质数因子
#     for i in range(2, int(number ** 0.5 + 2)):
#         if number % i == 0:
#             is_prime = False
#             print(str(i), end=" ")
#             # 递归继续查找
#             find_factors(int(number / i))
#             break
#     # 如果输入的数字本身就是质数，则直接输出（这也是递归出口）
#     if is_prime:
#         print(str(number), end=" ")
#
#     return
#
# try:
#      # 接收输入的整数
#     number = int(input())
#      # 如果输入的整数不符合正整数要求，抛出异常
#     if number <= 0:
#         raise Exception
#      # 调用自定义的find_factors函数，打印结果
#     find_factors(number)
#     # 对于程序中抛出的任何异常，捕获后程序直接结束
# except Exception as e:
#      exit()

# number=float(input())
# number=str(number).split(".")
# if int(number[1])<=5:
#     print(number[0])
# else:
#  print(int(number[0])+1)

import sys

# while True:
#
#         num=int(sys.stdin.readline().strip("\n"))
#         for i in range(1,num+1):
#             # index=int(sys.stdin.readline().strip(" "))
#             str1=sys.stdin.readline().strip("\n")
#             index=int(str1.split(" ")[0])
#             value=int(str1.split(" ")[1])
#         print(str(index)+" "+str(value))
#
#         break
from collections import defaultdict
# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1
# print(d)
# from collections import defaultdict
#
# while True:
#     try:
#
#         a, dd = int(input()), defaultdict(int)
#         for i in range(a):
#             key, val = map(int, input().split())
#             dd[key] += val
#         for i in sorted(dd.keys()):
#             print(str(i) + " " + str(dd[i]))
#
#
#     except:
#         break

# tempLine = []
# tempLine.extend((sys.stdin.readline().strip().split(' ')))
# print(tempLine)

# import sys
#
# n = int(input())
# key = []
# value = []
# dic = {}
# for i in range(n):
#     b = sys.stdin.readline().strip("\n").split(" ")
#     key.append(int(b[0]))
#     value.append(int(b[1]))
# #print(str(key)+" "+str(value))
# for i in range(len(key)):
#     if key[i] not in dic:
#         dic[key[i]] = value[i]
#     else:
#         dic[key[i]] += value[i]
# dic_sort = sorted(dic.items(), key=lambda x: x[0])
#
# for key, value in dic_sort:
#     print(str(key) + " " + str(value))

# num=int(input())
# str_number=[]
# for i in list(str(num)[::-1]):
#     if i not in str_number:
#         str_number.append(i)
#
# print("".join(str_number))

# str1=input()
# str2=""
# num=0
# for i in list(str1):
#     if i not in str2:
#         str2=str2.join(i)
#         num=num+1
# print(num)




# line=input()
# chars = set()
# for i in range(len(line)):
#     chars.add(line[i])
# print(len(chars))


# num=int(input())
# if num>=0:
#    num1=str(num)
#    print(num1[::-1])
# else:
#     print("输入值为非大于0的整数")

# import sys
# n=int(input())
# list_str=[]
# if n>=1 and n<=1000:
#    for i in range(n):
#     str1=sys.stdin.readline().strip()
#     list_str.append(str1)
# list_sort=sorted(list_str)
# for j in list_sort:
#     print(j)

# num=int(input())
# str_num=bin(num)
# str1="1"
# print(str_num.count(str1))

# import sys
# str1=sys.stdin.readline().strip().split(" ")
# n=int(str1[0])
# m=int(str1[1])
# v=[]
# p=[]
# q=[]
# toal=[]
# for i in range(m):
#     str2=sys.stdin.readline().strip("\n").split(" ")
#     v.append(int(str2[0]))
#     p.append(int(str2[1]))
#     q.append(int(str2[2]))
#
# for j in range(m):
#     toal_num=v[j]*p[j]
#     toal.append(toal_num)
# print(max(toal))



# def coordinate_shift(str1_list):
#     star = [0, 0]
#     for i in range(len(str1_list)):
#         pace = str1_list[i][1:]
#         if len(str1_list[i][:])>0 and pace.isdigit() and len(pace)>0 and len(pace)<=2:
#          if str1_list[i][0]=="A":
#             star[0]=star[0]-int(str1_list[i][1:])
#          elif str1_list[i][0]=="D":
#              star[0] = star[0]+int(str1_list[i][1:])
#          elif str1_list[i][0]=="W":
#              star[1] = star[1] + int(str1_list[i][1:])
#          elif str1_list[i][0]=="S":
#              star[1] = star[1] - int(str1_list[i][1:])
#         else:
#             star[0]=star[0]+0
#             star[1] = star[1] + 0
#     return star
#     # print(star)
#
# if __name__=="__main__":
#     str1 = input()
#     # str1 = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
#     str1_list = str1.split(";")
#     end=coordinate_shift(str1_list)
#     # print("{},{}".format(end[0],end[1]))
#     print(str(end[0])+"," + str(end[1]))

import sys
def check_len(s):
    if len(s)>8:
        return True
    else:
        return False
def check_num(s):
    is_low,is_up,is_digit,is_other=0,0,0,0
    for i in s:
        if i.islower():
            is_low=1
        elif i.isupper():
            is_up=1
        elif i.isdigit():
            is_digit=1
        else:
            is_other=1

    is_count = is_other + is_digit + is_low + is_up
    if is_count>=3:
        return True
    else:
        return False
def check_repeat(s):
    for i in range(len(s)-3):
        if s.count(s[i:i+3])>1:
            return False
        else:
            return True

while True:
    try:
        s=input()
        if check_len(s) and check_num(s) and check_repeat(s):
            print("ok")
        else:
            print("NG")
    except:
        break


