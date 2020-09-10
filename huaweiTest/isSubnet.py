#coding:utf-8

def ten_to_two(ip):
    """该函数是将ip地址转换成2进制"""
    ip_2=bin(int(ip)).replace("0b", "").rjust(8, "0")
    return ip_2
def two_to_ten(two):

   return int(two,2)

def check_ip(ip):
    """检查ip格式"""
    if len(ip) != 4 or '' in ip:
        return False
    else:
        is_ip = []
        for i in range(4):
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                is_ip.append(False)
            else:
                is_ip.append(True)
        if False in is_ip:
            return False
        else:
            return True

def check_is_ip(ip):
    if int(ip[0]) >= 1 and int(ip[0]) <= 126:
        return True
    elif 128 <= int(ip[0]) <= 191:
        return True
    elif 192 <= int(ip[0]) <= 223:
        return True
    elif 224 <= int(ip[0]) <= 239:
        return True
    elif 240 <= int(ip[0]) <= 255:
        return True
    elif int(ip[0])==10 or (int(ip[0])==172 and 15<int(ip[1])<32) or (int(ip[0])==192 and int(ip[1])==168):
        return True
    else:
        return False

def to_and(a,b):
    """a和b都为二进制 如11111111000000001111111100000000
    a为子网掩码，b为ip地址"""
    e=[]
    for i in range(32):
      e.append( a[i] and b[i])
    return "".join(e)


while True:
    try:
        """"""
        m="255.0.0.0 193.194.202.15 232.43.7.59"
        # line=input().split(" ")
        line=m.split(" ")
        line_a=line[0]
        line_b=line[1]
        line_c=line[2]
        line_list_b=line_b.split(".")
        list_a=[ten_to_two(x) for x in line_a.split(".")]
        list_b=[ten_to_two(x) for x in line_b.split(".")]
        list_c=[ten_to_two(x) for x in line_c.split(".")]
        if check_ip(line_a.split(".")):
          if "01" not in "".join(list_a):
             if check_ip(line_b.split(".")) and check_ip(line_c.split(".")):
                 if check_is_ip(line_b.split(".")) and check_is_ip(line_c.split(".")):
                        if to_and("".join(list_a),"".join(list_b))==to_and("".join(list_a),"".join(list_c)):
                            print(0)
                        else:
                            print(2)
                 else:
                     print(1)
             else:
                 print(1)
          else:
              print(1)
        else:
            print(1)


    except:
        break