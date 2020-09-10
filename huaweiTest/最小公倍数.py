def common_divisor_max(a,b):
    """求a b的最大公约数"""
    while (a!=b):
        if (a>b):
            a=a-b
        else:
            b=b-a
    return a

while True:
    try:
        line=input().split(" ")
        a=int(line[0])
        b=int(line[1])
        print(int(a*b/(common_divisor_max(a,b))))
    except:
        break