import sys

# while True:
#     try:
#         # s = input()
#         s="df22 rdff"
#         t=""
#         for i in range(len(s)):
#             if s[i].isalpha():
#                 t= t + s[i]
#         tt = sorted(t,key=str.upper)
#         print(tt)
#         result = ""
#         index = 0
#         for i in range(len(s)):
#             if s[i].isalpha():
#                 result = result + tt[index]
#                 index = index + 1
#             else:
#                 result = result + s[i]
#         print(result)
#     except:
#         break

mo="3 abc bca cab abc 1"
# L = input().split(' ')
L=mo.split(" ")
n = int(L[0])
m = int(L[-1])
line = L[-2]
li = ''.join(sorted(line))
L = L[1:-2]
LL = [''.join(sorted(list(x))) for x in L]
num = LL.count(li) - L.count(line)
print(num)

zd = []
for i in range(len(LL)):
    if li == LL[i] and line != L[i]:
        zd.append(L[i])

if num >= m:
    for i in range(len(line)):
        zd = sorted(zd, key=lambda x: x[len(line) - i - 1])
    print(zd[m - 1])

