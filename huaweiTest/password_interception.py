#coding:utf-8

"""返回有效密码串的最大长度"""
while True:
    try:

        line=input()
        if "123321" in line:
            password_len=6
        elif "ABBA" in line:
            password_len=4
        elif "ABA"  in line:
            password_len=3
        elif "A" in line:
            password_len=1
        else:
            password_len=0

        print(password_len)
    except:
        break