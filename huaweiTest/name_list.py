def beautiful(lis):
    dic = {}
    lis = lis.upper()
    for i in lis:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    val = list(dic.values())
    val.sort(reverse=True)
    weight = list(range(1, 27))
    weight.sort(reverse=True)
    sum1 = 0
    for i, j in zip(val, weight):
        sum1 = sum1 + i * j
    return sum1


def beautiful_lis(s_lis):
    a = []
    for i in s_lis:
        a.append(beautiful(i))
    return a


while True:
    try:
        n = int(input())
        name_lis = []
        # name_lis=["zhangsan","lisi"]
        for i in range(n):
            name_lis.append(input())

        val = beautiful_lis(name_lis)
        for i in val:
            print(i)
    except:
        break