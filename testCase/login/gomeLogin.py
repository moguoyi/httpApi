import requests
from httpApi.commons.headerToParm import *
import  json

class Login(object):
    url=ConfigParsers().URL
    postHeader=ConfigParsers().postHeader()
    @staticmethod
    def insertAddress():

        # url = "https://member.gome.com.cn/myaccount/address/insertAddress?timer=1574694852519&callback=ckdata&firstName=223&address=2234&mobile=18513827507&state=11000000&city=11010000&county=11010200&town=110102002&isDefault=false&isQuicklyBuy=false&_=1574694852519"

        querystring = {"timer": "1574691456258", "callback": "ckdata", "firstName": "0922123w", "address": "2222",
                       "mobile": "18513827507", "state": "11000000", "city": "11010000", "county": "11010200",
                       "town": "110102002", "isDefault": "false", "isQuicklyBuy": "false"}
        url = "https://member.gome.com.cn/myaccount/address/insertAddress"
        headers = {
            'cookie': 'uid=CnMjWl3b4eqwclX0zpFhAg==; sajssdk_2015_cross_new_user=1; s_cc=true; atgregion=11010200%7C%E5%8C%97%E4%BA%AC%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%9C%9D%E5%A4%96%E8%A1%97%E9%81%93%7C11010000%7C11000000%7C110102002; cartnum=0_0-1_0; _idusin=82773656295; __clickidc=196333630874691270; __c_visitor=196333630874691270; __gma=ffb8de7.1076044964939.1574691270874.1574691270874.1574691270874.1; __gmc=ffb8de7; __gmv=1076044964939.1574691270874; ufpd=2722565485634821c98ea2c534d83063b92b95ff9cb606a145218995cda08c3ca218b6e1187f917d3a3ae56bfdebd404e74dbf197ab6bcdbb3331566c42b00af|5ddbe208gRCKFSHIgZvoSlqayBeXL3jBggEbOPW1; _smt_uid=5ddbe1ca.32f4eda5; SCN=apsQrhlgqqZJ7Z5SQVFQ7mAAG5sTZf3LLXc%2BdlH3o9atuZVXUfoxsTGeKkDxnkWfSJ4zFNkUA7kJ291hj94VQr9vd5lgXYxVEnrhQMKnPrlT8zZ2K0IzEg%3D%3D35d51f80f1b563cd25e1ad88a1046bce; sid=72001368571; SSO_USER_ID=72001368571; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2272001368571%22%2C%22%24device_id%22%3A%2216ea2e9c2e5a8f-0aec334a1110fe-1c3b6a5b-1296000-16ea2e9c2e681b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216ea2e9c2e5a8f-0aec334a1110fe-1c3b6a5b-1296000-16ea2e9c2e681b%22%7D; DSESSIONID=7fadd85ca1474e90841b77ee496a5ee5; s_ppv=-%2C33%2C33%2C705; s_getNewRepeat=1574691333128-New; s_sq=gome-prd%3D%2526pid%253D%2525E7%252594%2525A8%2525E6%252588%2525B7%2525E4%2525B8%2525AD%2525E5%2525BF%252583%25253A%2525E4%2525BC%25259A%2525E5%252591%252598%2525E4%2525BF%2525B1%2525E4%2525B9%252590%2525E9%252583%2525A8-%2525E6%252588%252591%2525E7%25259A%252584%2525E5%25259B%2525BD%2525E7%2525BE%25258E%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fmyhome.gome.com.cn%25252Fmember%25252FaddressPage%2526ot%253DA',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.3',
            'content-type': "text/plain;charset=UTF-8",
            'Accept':'*/*',
            'referer':'https://myhome.gome.com.cn/member/addressPage',
        }

        response = requests.get(url, headers=headers,params=querystring)

        print(response.text)

if __name__=="__main__":
    Login.insertAddress()
