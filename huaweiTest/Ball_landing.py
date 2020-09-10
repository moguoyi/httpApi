while True:
    try:
        n=int(input())
        # n=2
        sum_n=n
        for i in range(1,5):
            m=n*(2/2**i)
            sum_n=sum_n+m
        print(sum_n)

        # print(round(n * 23 / float(8), 3))
        # print(n / 32)

    except:
      break
