#!/usr/bin/evn python3
# -*- coding:utf-8 -*
import requests
import re
import json
# from bs4 import BeautifulSoup

url = "https://www.imooc.com/u/card%20"

querystring = {"jsonpcallback":"jQuery19109376988968996445_1563039803905","_":"1563039803906"}

headers = {
   'Host':'www.imooc.com',
   'Connection':'keep-alive',
   'X-Requested-With':'XMLHttpRequest',
   'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
   'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
   'Referer':'https://www.imooc.com/search/?words=%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95&page=2',
   'Accept-Encoding':'gzip, deflate, br',
   'Accept-Language':'zh-CN,zh;q=0.9',
   'Cookie':'imooc_uuid=28aa5427-416e-4a10-a5fb-12eee6502df7; imooc_isnew_ct=1553088082; zg_did=%7B%22did%22%3A%20%221699b4377115e7-013b20b0dd29aa-36647105-13c680-1699b4377123d6%22%7D; imooc_isnew=2; mc_channel=bdxcx; mc_marking=c89d21283b1ec97c356d3c37eb94157d; UM_distinctid=16be9d84196838-07fe3e8a7395aa-37677e02-13c680-16be9d841973d9; CNZZDATA1261110065=1225237676-1562991239-https%253A%252F%252Fwww.baidu.com%252F%7C1562991239; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1562996397; IMCDNS=0; loginstate=1; apsid=gxYmI3NjZjYmIxYTJiYzI2Y2VkNWU5NGU1NjVmMjMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMzQxODk2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGJmMmM3YTc3ODhhMzAzMGRiNWFhY2U1YWY0OGYwZjllCf8pXQn%2FKV0%3DZD; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1563034327; cvde=5d296ed0e8d0f-61; zg_f375fe2f71e542a4b890d9a620f9fb32=%7B%22sid%22%3A%201563039803779%2C%22updated%22%3A%201563039803817%2C%22info%22%3A%201562996397748%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E6%85%95%E8%AF%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E7%BB%9F%E8%AE%A1%5C%22%2C%5C%22Platform%5C%22%3A%20%5C%22web%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.imooc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201563039803779%2C%22cuid%22%3A%20%22iEpgmGAjrOk%2C%22%7D'
    }



response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.encoding)
# print(response.encoding)  # ISO-8859-1
# response.encoding = 'gbk'  # 指定页面编码方式
# soup = BeautifulSoup(response.text, 'lxml')
# mo=response.json()['data']['course_name']
# print(soup)
#转码

mo=response.content.decode("unicode_escape")
# yi=response.json.loads(response,encoding='utf-8')
# info=eval(mo)
# json
print(mo)
# mo=mo.split("(",1)
# mo=mo[1].split(")",1)
# print(type(mo[0]))
# print(mo[0])
# mo=eval(mo[0])
mo=eval(re.split(r'[()]',mo)[1])
print(mo)
print(mo.get("data").get("nickname"))

if mo.get("msg")=="成功":
   print("登录成功，msg日志为{}".format(mo.get("msg")))