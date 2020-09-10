
"""有一只兔子，从出生后第3个月起每个月都生一只兔子，
小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，
问每个月的兔子总数为多少？"""
while True:
    try:
        # month=int(input())
        month=6
        if month<3:
            print(1)
        else:
            a=1
            b=1
            for i in range(3,month+1):
                a,b=b,a+b
                # a=b
                # b=a+b

            print(b)
    except:
        break