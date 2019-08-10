#!/usr/bin/evn python
# -*- coding:utf-8 -*

import urllib
import urllib2
import json

url="http://127.0.0.1:8000/login_action/"
headers={
   'Host': '127.0.0.1:8000',
   'Connection':'keep-alive',
   'Content-Length': '120',
   'Cache-Control':'max-age=0',
   'Origin':'http://127.0.0.1:8000',
   'Upgrade-Insecure-Requests':'1',
   'Content-Type':'application/x-www-form-urlencoded',
   'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
   'Referer':'http://127.0.0.1:8000/',
   'Accept-Encoding':'gzip, deflate, br',
   'Accept-Language':'zh-CN,zh;q=0.9',
   'Cookie':'sessionid=6i6cfz6ldomwshimqf6pk1yru92wwiry'
}
data={}
data['username']='admin'
data['password']='admin123456'
data['csrfmiddlewaretoken']='Wu8yKR4Kv4ENTnZQyyAnYcmiL7CJEDYm3Y286osAO31i1Hl2dHPUbLIVii2ywGu7'
#数据编码及赋值
data=urllib.urlencode(data)
req=urllib2.Request(url,data,headers)
#打开地址
responseStr=urllib2.urlopen(req)
# json.load(responseStr)
sta=responseStr.code
if sta==200:
#读取获得的值
 responseStr=responseStr.read()

#打印
#转码
# responseStr=responseStr.decode('unicode_escape')
 print responseStr
else:
    print sta
