#coding:utf-8

# while True:
#     try:
#         """蛇形矩阵"""
#         # n=int(input())
#         n=4
#         a = 1
#         b=2
#         for i in range(n):
#             a+=i
#             print("{}".format(a),end=' ')
#             pre=a
#             for j in range(n-i-1):
#                 print("{}".format(j+b+pre),end=' ')
#                 pre=pre+b+j
#             b=b+1
#             print()
#
#     except:
#         break


# while True:
#     try:
# num=int(input())
num=4
L=[[0 for i in range(0)] for j in range(num)]
insert=1;
for i in range(num):
    for j in range(i,-1,-1):
        L[i-j].append(str(insert))
        insert=insert+1
for i in range(num):
    print(' '.join(L[i]))
#     # except:
    #     break


