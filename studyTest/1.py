
num = int(input('请输入一个四位数：'))
while True:
    if len(str(num))==4:
        ge = num % 10
        ten = num%100//10
        hu = num//100%10
        th = num // 1000

        ge1 = ge + 5
        ge2 = ge1 % 10

        ten1 = ten + 5
        ten2 = ten1 % 10

        hu1 = hu + 5
        hu2 = hu1 % 10

        th1 = th + 5
        th2 = th1 % 10

        print('加密后的数为：',int((str(ge2)+str(ten2)+str(hu2)+str(th2))))
        break
    num = int(input('您输入的位数有误，请重新输入：'))

