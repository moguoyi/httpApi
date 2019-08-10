#!/usr/bin/env python3
# -*- conding:utf-8 -*-
import requests
import sys, io
# 解决console显示乱码的编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

login_url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
userinfo = {
    "loginType":"1",
    "pwdOrVerifyCode":"mgy123456789",
    "userIdentification":"18513827507",
    "uaToken": "118#ZVWZz4Rd7hsQDegoje2S/ZZTZsgh1HdXZH2zebZhzHWzZgYjVfq4ge2zRgghyHRVZg2LZs6hzQGuZWNCVfqVzH2z8ZZTVbTagexKus6hzHRzZI2uVnq4KT2zZ4QaVHR4Zg2ZYsqTzfQZZezHhGiWtmgMUhXDHZAzZZx1ZOiTzeWzZgCuc5qYNG9wpeChXHRYzH2ZZwqh4XGizZZZXTNVzH2zuZbTVHRVZZ2uZYqhzHRZZgFZVoq4zH2ZZ0qTVHRVZzWZg1ZhzeWzZgZ7TURVneVAZCRTBHR7geYCozu2U+L26lJj+DjdRJPtQ6windtX+UuKAcdHzYMsPy8lvmXAnPaeVHBR61QJchyS2Ad9QNuLruPD6ZR5IZVScHQZuYPAPQqZZyj1zsXk+yAZX5cEW9/N2jvrrEqt7hQPAj1R9da6X9LYHeWaAsf87zS5OM52x2vXm9IFoaSbnTCN4wENP2bwPhvbyMbkPFN/c6eRUwxTMSYXz22EkNQ52BAiEHbYoxlX6Wwo/8GQkRaLKvyPP+kYVhK0+I7uLY8+0F0yS5ilMdD+coP3pmJQeGQ38/js351SjRjT8FAzP8mWOqbNJXEHLnEIQtCwy4dNlergb7JgTARWFPmW9oI5lRcTFi81Nj+1EWO1brBGzuJjFjnsD9iZ8k2AWh6mXBFe3VdsUX/Y0EMH6sFEl54eOFn5PlMlyMEmYnJOSvKLkj1lcVjlBrMdogf1ifR6r6WqLlXKJMmadyWuwr6OQCez1VFdY63aBIMSyu7u5QSPGZfKR9UhVINrtFlH+kXRCnL1GmumQFptJrNrVn+igBlpw9fiKS9R4woe0YoJjbEfj/ED+876/aaJRP8rKAWZKE2S4mbHKs4jhJ08ws5TDzuWB0SLeQkLftGc4mA7tQsBaEiOy22a58T2DrIiV7h47PIVPuz/OGC7ed4InhJ5f+Lm8GLspaAWfSL77MH/kNOOXY5s4iqd3i23xnZIEfEys62gm/lfg8ILvmryJs9PnL3Owe2YSlAvuNyuzk8PoU/iUs0p9DUbm78/bbyx/S73nAsOGyaBD4zOD3vbS2V3jZHQRvpoGU1wF8zvfuSqc8XfiAzh5CP21P9kRIdP1PHDRv+2yD5zKma0GSccsSCqw4YMlWNAkF/aWzA8KY35kxpd3nQVIsUTNXyDjHKrbrB/Es3xDF79UAVu3jDEIz0mhEJBEco7LZn+z0JtDmqXWYvfyoYfkS/2BE7W7ATyB6fUNOg2nVhBAofNPydxiphR6cXrQKvroaK+jP6MdLdYUZuxJSQ2wiu+j3CihJkKXvZ8KCmhX8zb30jucNR/yaIEy9fuD34QhGYHd97pA/KS3oLUZ13Av7/sCNvQdeaZL5zwQak5ZhIZLq/ZrJfo5x/JoZw/sEqzX6I6odyE3FRsYPYBRhecX1bB8F/ftk7r1wctZwUZKaq=",
	"webUmidToken": "TCE55AC0C93A42F130BD2551F26E83C0296110316E5648D7A8FA30829F2"
}
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
'Referer':'https://passport.csdn.net/login',
}

response = requests.post(url=login_url, data=userinfo, headers=headers,verify=False).content.decode('utf-8')
# 获取登录后的cookies内容
# cookies = response.cookies
# print(cookies)
print(response)

# myaddress_url = 'https://msg.csdn.net/v1/web/message/view/message'
# myaddress = requests.get(myaddress_url, cookies=cookies)  # 在请求中带入cookies
# print(myaddress.status_code)
# print(myaddress.text)