import  sys
# while True:
#     try:
# count=0
# n=int(input())
# student=sys.stdin.readline().strip("\n").split(" ")
# print(student)
# for i in student:
#     if i>=i+1:
#         print(student[i])
#         student.remove(student[i])
#         count+=1
#
# print(count)
    # except:
    #     break


# n = int(input())
# # key = []
# # value = []
# # dic = {}
# # for i in range(n):
# b = sys.stdin.readline().strip("\n").split(" ")
#
# print(b)



# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))


import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
# if __name__ == "__main__":
#






# if __name__ == "__main__":
n = int(sys.stdin.readline().strip())
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()

values1 = line1.split(",")
values2 = line2.split(",")

len1 = len(values1)
len2 = len(values2)

def input_in(s,len_one):
    """"""
    if 0<len_one<n:
        s.extend("x"*(n-len_one))
    else:
        if len_one%n!=0:
            s.extend("x" * (n - (len_one%n)))
    return s
new_values1=input_in(values1,len1)
new_values2=input_in(values2,len2)
new_lsit=[]
if len(new_values1)>=len(new_values2):
    for i in range(len(new_values1)//n):
        new_lsit.extend(new_values1[i*n:i*n+n])
        new_lsit.extend(new_values2[i*n:i*n+n])
else:
    for i in range(len(new_values2)//n):
        new_lsit.extend(new_values1[i*n:i*n+n])
        new_lsit.extend(new_values2[i*n:i*n+n])

new_lsit1="".join(new_lsit)

print(new_lsit1.replace("x",""))





