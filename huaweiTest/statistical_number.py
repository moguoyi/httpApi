#coding:utf-8
"""统计字母、数字、空格的数字"""
while True:
    try:
        line=input()
        num=0
        digit=0
        space=0
        other=0
        for i in line:
            if i.isalpha():
                num+=1
            elif i.isdigit():
                digit+=1
            elif i.isspace():
                space+=1
            else:
                other+=1
        print("{}\n{}\n{}\n{}".format(num,space,digit,other))
    except:
        break