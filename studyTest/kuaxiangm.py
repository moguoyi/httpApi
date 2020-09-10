import os
import sys

from httpApi.commons.getConfig import GetConfig




print(GetConfig().read_value("parameter","url"))

# /Users/moguoyi/pyStudy/httpApi/file/conf.ini
print(GetConfig().read_value("parameter","url"))

print(GetConfig().read_value("parameter","url","/Users/moguoyi/pyStudy/httpApi/file/conf.ini"))
# GetConfig.read_value()
