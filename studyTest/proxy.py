import requests
from httpApi.studyTest import readJson


url = 'https://www.baidu.com'


header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

free_proxy = {
#都是http类型地址
##'http': '163.204.241.160:9999'
'http': '123.206.54.52:8118'
    }

response = requests.get(url=url, headers=header, proxies=free_proxy).text
print(response)
# print(readJson.OperetionJson("name").get_data())



