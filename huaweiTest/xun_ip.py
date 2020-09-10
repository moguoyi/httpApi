def check_ip(ip):
    """检查ip格式"""

    if len(ip) !=4 or '' in ip:
        return False
    else:
        is_ip = []
        for i in range(4):
            if int(ip[i])<0 or int(ip[i])>255:
                 is_ip.append(False)
            else:
                is_ip.append(True)
        if False in is_ip:
            return False
        else:
            return True


