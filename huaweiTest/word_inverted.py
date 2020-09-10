import re
while True:
    try:
        line = input()
        FILTER_PUNTS = re.compile("[^^a-z|^A-Z]")
        text = FILTER_PUNTS.sub(" ", line.strip())
        line=text.split()
        print(' '.join(line[::-1]))
    except:
        break


# coding: utf-8
# import re
# text = "aa[bb5aa#cWc中a国"
# FILTER_PUNTS = re.compile("[^^a-z|^A-Z]")
# text = FILTER_PUNTS.sub(" ", text.strip())
# print(text)