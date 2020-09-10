#coding:utf-8
import json
import requests

class BuyTicketLogin():

    """登录12306账户获取cookie的值"""
    def login(self):
        # https: //kyfw.12306.cn / passport / web / login
        url="https://kyfw.12306.cn/passport/web/login"
        data={"username":"mgy543622257",
              "password":"mgy1004495171",
              "appid":"otn",
              "answer":"48,120,186,120"}
        headers = {
            # 'cookie': '__clickidc=196333630874691270; __c_visitor=196333630874691270; __gmv=1076044964939.1574691270874; _dx_uzZo5y=cfa7a978daf519f0ee93953171056554fce299b25569881b72bb2573f94331bceb38b848; _smt_uid=5ddbe1ca.32f4eda5; sid=72001368571; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2272001368571%22%2C%22%24device_id%22%3A%2216ea2e9c2e5a8f-0aec334a1110fe-1c3b6a5b-1296000-16ea2e9c2e681b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216ea2e9c2e5a8f-0aec334a1110fe-1c3b6a5b-1296000-16ea2e9c2e681b%22%7D; uid=CjozJ14Qu6dTtcEmsACPAg==; ctx=app-shangcheng|ver-1.0|plt-pc|cmpid-; s_cc=true; gpv_p22=no%20value; atgregion=22010200%7C%E6%B5%99%E6%B1%9F%E7%9C%81%E6%9D%AD%E5%B7%9E%E5%B8%82%E4%B8%8A%E5%9F%8E%E5%8C%BA%E6%B9%96%E6%BB%A8%E8%A1%97%E9%81%93%7C22010000%7C22000000%7C220102001; cartnum=0_0-1_0; DSESSIONID=5166db490b5045e38b6a5d3fa7ca08e4; _idusin=83204907238; JSESSIONID=1baqtu6sk9sznzvsjyhom75sn; isnew=35184385075.1578154970978; __gma=ffb8de7.1076044964939.1574691270874.1574691270874.1578154970986.2; __gmb=ffb8de7.1.1076044964939|2.1578154970986; __gmz=ffb8de7|www.gome.com.cn|-|referrer|-|-|-|1076044964939.1574691270874|dc-1|1578154970988; __gmc=ffb8de7; gpv_pn=%E5%9B%BD%E7%BE%8E%E7%99%BB%E5%BD%95; ufpd=1530d6522a0845b92087387e00934cc588a3d745c3b3c66516640bc45f901f4da5a752d5478ae535bd2fed23d363f9ffe370b2ae5bce167958a6fc8f054b84b8|5e10bbeberSoCEymNxph7Gko8u9HMs2L9sYigNy1; ufpd=1530d6522a0845b92087387e00934cc588a3d745c3b3c66516640bc45f901f4da5a752d5478ae535bd2fed23d363f9ffe370b2ae5bce167958a6fc8f054b84b8|5e10bbeberSoCEymNxph7Gko8u9HMs2L9sYigNy1; s_ppv=-%2C68%2C50%2C578; distinctId=72001368571; plasttime=1578155001; s_getNewRepeat=1578155000637-Repeat; s_sq=gome-prd%3D%2526pid%253D%2525E5%25259B%2525BD%2525E7%2525BE%25258E%2525E7%252599%2525BB%2525E5%2525BD%252595%2526pidt%253D1%2526oid%253Dfunctiononclick(event)%25257BloginGome(preLogin)%25253Breturnfalse%25253B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.3',
            'content-type': "application/x-www-form-urlencoded",
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'referer': 'https://login.gome.com.cn/login?intcmp=sy-public01012'
        }
        # data=json.
        result=requests.post(url,data=data,headers=headers,verify=False).text
        print(result)

if __name__=="__main__":
    BuyTicketLogin=BuyTicketLogin()
    BuyTicketLogin.login()