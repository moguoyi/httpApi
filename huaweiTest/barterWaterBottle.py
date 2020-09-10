#codding:utf-8
import sys
"""
这个是用测试3个空瓶换一个水瓶
"""
# n=int(input())
# # n=1
# num_one=[]
# for i in range(n):
#     num=int(sys.stdin.readline().strip())
#     num_one.append(num)
#     # num=4
#
# for i in range(n):
#     if num_one[i]>=3:
#         if num_one[i]%3==0:
#          # print(num/3)
#          n1=num_one[i]//3
#         elif num_one[i]%3==2:
#             num1=num_one[i]//3
#             # print(num1+1)
#             n1=num1+1
#         else:
#             n1=num_one[i]//3
#             # print(num//3)
#         print(n1)
#     else:
#         print(0)

import sys
while True:
    try:
        line = int(sys.stdin.readline().strip())
        if line > 0:
            count = 0
            while line > 1:
                if line <= 3:
                    count += 1
                    break
                else:
                    more = line//3
                    count += more
                    line -= more*2
            print(count)
        else:
            break
    except:
        break