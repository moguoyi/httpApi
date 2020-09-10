#coding:utf-8

while True:
    try:
      line=input()
      print("".join(sorted(line)))
    except:
        break


# print(int("".join(map(lambda c:bin(c).replace("0b","").rjust(8,"0"),map(int,input().split(".")))),2))

