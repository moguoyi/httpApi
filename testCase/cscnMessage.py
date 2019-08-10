#!/usr/bin/evn python3
# -*- coding:utf-8 -*-
import requests
import sys, io
# 解决console显示乱码的编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://msg.csdn.net/v1/web/message/view/message'
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
'Referer':'https://i.csdn.net/',
}
# 修改'type'，'source'参数值验证参数合法性
post_data = {
	'pageIndex':'1',
	'pageSize':'15',
    'type':'0'
}

response = requests.post(url=url, data=post_data, headers=headers).content.decode('utf-8')
print('result:\n', response)



