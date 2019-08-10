#!/usr/bin/env python3
# -*- conding:utf-8 -*-
import requests

url = "https://passport.cnblogs.com/user/signin"  # 接口地址

# 消息头数据
headers = {
    'Connection': 'keep-alive',
    'Content-Length': '123',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://passport.cnblogs.com/user/signin',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://passport.csdn.net/account/login?from=http://www.csdn.net',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '省略'

}

payload = {'username': '莫忆13',
           'password': 'mgy123456,',
           'lt': '**',
           'execution': 'e1s1',
           '_eventId': 'submit'

           }
# verify = False 忽略SSH 验证


r = requests.post(url, data=payload, headers=headers, verify=False)
print
r.json()
