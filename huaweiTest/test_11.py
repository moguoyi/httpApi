def letter_encryption(letter):
    """对字母的加密"""
    if letter.islower():
        if letter == "z":
            letter = "A"
        else:
            letter = chr(ord(letter) + 1).upper()
    else:
        if letter == "Z":
            letter = "a"
        else:
            letter = chr(ord(letter) + 1).lower()
    return letter


def letter_decryption(letter):
    """对字母的解密方法"""
    if letter.islower():
        if letter == "a":
            letter = "Z"
        else:
            letter = chr(ord(letter) - 1).upper()
    else:
        if letter == "A":
            letter = "z"
        else:
            letter = chr(ord(letter) - 1).lower()
    return letter


def digit_encryption(num):
    """对数字的加密方法"""
    if num == 9:
        num_input = 0
    else:
        num_input = num + 1
    return str(num_input)


def digit_decryption(num):
    """对数字的解密方法"""
    if num == 0:
        num_input = 9
    else:
        num_input = num - 1
    return str(num_input)

while True:
    try:
        lien_a=input()
        line_b=input()
        # lien_a = "DSFDF33"
        # line_b = "DDFWWss3"
        a=[]
        b=[]
        for i in lien_a:
            if i.isalpha():
                io=letter_encryption(i)
                a.append(io)
            else:
                io=digit_encryption(int(i))
                a.append(io)

        for j in line_b:
            if j.isalpha():
                jo=letter_decryption(j)
                b.append(jo)
            else:
                jo=digit_decryption(int(j))
                b.append(jo)
        print("".join(a))
        print("".join(b))

    except:
        break