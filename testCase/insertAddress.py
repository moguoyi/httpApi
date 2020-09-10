import requests
from locust import HttpLocust, TaskSet, task

class InsertAddress(TaskSet):
    headers = {
        'cookie': '__clickidc=196333630874691270; __c_visitor=196333630874691270; __gmv=1076044964939.1574691270874; _smt_uid=5ddbe1ca.32f4eda5; sid=72001368571; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2272001368571%22%2C%22%24device_id%22%3A%2216ea2e9c2e5a8f-0aec334a1110fe-1c3b6a5b-1296000-16ea2e9c2e681b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216ea2e9c2e5a8f-0aec334a1110fe-1c3b6a5b-1296000-16ea2e9c2e681b%22%7D; uid=CjozJ14Qu6dTtcEmsACPAg==; ctx=app-shangcheng|ver-1.0|plt-pc|cmpid-; s_cc=true; atgregion=22010200%7C%E6%B5%99%E6%B1%9F%E7%9C%81%E6%9D%AD%E5%B7%9E%E5%B8%82%E4%B8%8A%E5%9F%8E%E5%8C%BA%E6%B9%96%E6%BB%A8%E8%A1%97%E9%81%93%7C22010000%7C22000000%7C220102001; cartnum=0_0-1_0; _idusin=83204907238; __gmc=ffb8de7; __gma=ffb8de7.1076044964939.1574691270874.1578159426088.1578214021393.4; __gmz=ffb8de7|myhome.gome.com.cn|-|referrer|-|-|-|1076044964939.1574691270874|dc-1|1578214021397; gpv_pn=%E5%9B%BD%E7%BE%8E%E7%99%BB%E5%BD%95; gpv_p22=no%20value; __gmb=ffb8de7.2.1076044964939|4.1578214021393; s_getNewRepeat=1578214041100-Repeat; s_sq=gome-prd%3D%2526pid%253D%2525E5%25259B%2525BD%2525E7%2525BE%25258E%2525E7%252599%2525BB%2525E5%2525BD%252595%2526pidt%253D1%2526oid%253Dfunctiononclick(event)%25257BloginGome(preLogin)%25253Breturnfalse%25253B%25257D%2526oidt%253D2%2526ot%253DBUTTON; ufpd=071d1b8b89f96806efe63a58111a257544aedcf531f11f864b46571e28b75c134e8fb00ac8971cc390d116fa61a04bc437642892472c183c662b907ba6eeb948|5e10bbeberSoCEymNxph7Gko8u9HMs2L9sYigNy1; s_ppv=-%2C60%2C60%2C507; SCN=apsQrhlgqqZJ7Z5SQVFQ7mAAG5sTZf3LLXc%2BdlH3o9atuZVXUfoxsTGeKkDxnkWfM%2Bd7kK6rAKac2nbytUMYAfrqV8Dz0hZN1P0ECO8glre7JE8%2FKu%2BpUg%3D%3D1915c6ec5942b32c666ba1a0575c2b6a; SSO_USER_ID=72001368571; DSESSIONID=d9c108770cbd4e3993ef1170effbbf23',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.3',
        'content-type': "text/plain;charset=UTF-8",
        'Accept': '*/*',
        'referer': 'https://myhome.gome.com.cn/member/addressPage',
    }

    @task
    def insertAddres(self):
        querystring = {"timer": "1574691456258", "callback": "ckdata", "firstName": "0922123w", "address": "2222",
                       "mobile": "18513827507", "state": "11000000", "city": "11010000", "county": "11010200",
                       "town": "110102002", "isDefault": "false", "isQuicklyBuy": "false"}
        url = "/myaccount/address/insertAddress"

        self.client.get(url, headers=self.headers, params=querystring,timeout=10)



        # print(response.text)

class UserOne(HttpLocust):
    task_set = InsertAddress
    weight = 1
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 5
    host = "https://member.gome.com.cn"