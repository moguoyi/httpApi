#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
line = "This is a regular expression for python"
matchObj = re.match(r'(.*) is (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.span() :",matchObj.span())
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups()) :", matchObj.groups())
else:
    print("No match!!")
