while True:
    try:
        a,n = input().split()
        n = int(n)
        if a[n-1].isalpha():
            print(a[:n])
        else:
            print(a[:n-1])
    except:
        break

# print(len('12'.encode('gbk')))


