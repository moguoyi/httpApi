def str_orde(string):
    """进行排序"""
    a=[]
    b=[]
    c=[]
    for i in range(1,len(string)+1):
        if i%2==0:
            a.append(string[i-1])
        else:
            b.append(string[i-1])
    new_a = sorted(a)
    new_b = sorted(b)
    if len(a)>len(b):
        len1=len(a)
        new_b.extend("*"*(len(a)-len(b)))
    else:
        len1=len(b)
        new_a.extend("*" * (len(b) - len(a)))

    for j in range(len1):
        c.append(new_b[j])
        c.append(new_a[j])
    #返回字符串
    str_c="".join(c)
    return str_c.replace("*","")


def str_Transformation(char):
    """对字符进行转化"""
    char10 = int(char, 16)
    #16进制转换成2进制得出0b1010的二进制字符串
    if char.isdigit():
        char2=list(bin(char10))
        nop=char2.index("b")
        if len(char2)==3:
         char2.insert(nop+1,"0"*3)
        elif len(char2)==4:
            char2.insert(nop + 1, "0" * 2)
        elif len(char2)==5:
            char2.insert(nop + 1, "0")
        char3="".join(char2)
    else:
        char3=bin(char10)
        #对二进制字符串进行翻转（只翻转1010部分）
    newchar="0b"+char3[::-1][:-2]
    #翻转结束后,先进行转换成10进制再将数据转换成16进制
    newchar10=int(newchar,2)
    newchar16=hex(newchar10)
    #返回16进制数据 去掉0x 的大写
    return newchar16[2].upper()


while True:
    try:
        line=input()
        # line="oc645 eQjgJX"
        newline=line.replace(" ","")
        order_line=str_orde(newline)
        transformation=[]
        is_num="ABCDEFabcdef"
        for i in order_line:
            if i.isdigit() or (i in is_num):
                transformation.append(str_Transformation(i))
            else:
                transformation.append(i)
        print("".join(transformation))

    except:
        break


