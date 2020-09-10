# #统计字符个数
while True:
  try:
    line=input()
    resoult={}
    max_str=[]
    for i in line:
        resoult[i]=line.count(i)
    # print(resoult)
    for key,value in resoult.items():
        if (value == min(resoult.values())):
            max_str.append(key)
    # print(max_str)
    # for i in range(len(line)):
    for j in max_str:
        # print(j)
        line=line.replace(j,"")

    print(line)
  except:
      break





