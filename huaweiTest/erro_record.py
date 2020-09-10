import sys


# def get_name_col(str1):
#     """"""
#
# def get_file_name(name):
#
#     if len(name)>16:
#         file_name=name[-16:]
#     else:
#         file_name=name
#     return file_name
#
# str=sys.stdin.readline().strip()

import sys
d={}
name=[]
while True:
    try:
        v=input().split(' ')
        # v=sys.stdin.readline().strip()
        a=v[0].split('\\')[-1]
        if len(a)>=16:
            a=a[-16:]
        else:
            pass
        v1=a+' '+str(v[-1])
        if v1 not in d.keys():
            name.append(v1)
            d[v1]=1
        else:
            d[v1]+=1
    except:
        break
for item in name[-8:]:
    sys.stdout.write(item+' '+str(d[item])+'\n')