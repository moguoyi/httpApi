#coding:utf-8

"""该脚本为整数与ip地址之间的转换"""
while True:
    try:

        line_a=input().split(".")
        line_b=input()
        a=[]
        """将line_a的10进制装换成二进制"""
        for i in line_a:
            line_a_2=bin(int(i)).replace("0b","").rjust(8,"0")
            a.append(line_a_2)
        newstring="".join(a)
        """二进制转码成10进制"""
        new_10=int(newstring,2)
        print(new_10)

        """下面10进制转化成ip"""
        new_2=bin(int(line_b)).replace("0b","").rjust(32,"0")
        # print(new_2)
        str1=str(int(new_2[:8],2))
        str2=str(int(new_2[8:16],2))
        str3=str(int(new_2[16:24],2))
        str4=str(int(new_2[24:],2))
        print(str1+"."+str2+"."+str3+"."+str4)
    except:
         break
