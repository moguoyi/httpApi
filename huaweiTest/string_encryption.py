#coding:utf-8

def key_table(key):
    """根据秘钥获取秘钥表(返回字典类型格式)"""
    start_key=[chr(x) for x in range(65,91)]
    end_key=[]
    for i in key:
        if i.upper() not in end_key:
            end_key.append(i.upper())
    for j in range(26):
        if start_key[j] not in end_key:
            end_key.append(start_key[j])
    return dict(map(lambda x,y:[x,y],start_key,end_key))

while True:
    try:
        key = input()
        key_dict = key_table(key)
        plaintext = input()
        encrypt = []
        for i in plaintext:
            if i.isupper():
                encrypt.append(key_dict.get(i))
            else:
                encrypt.append(key_dict.get(i.upper()).lower())
        print("".join(encrypt))
    except:
        break




