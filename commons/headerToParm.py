import configparser
import os

class ConfigParsers(object):
    cf = configparser.ConfigParser()
    # file="/Users/moguoyi/pyStudy/httpApi/conf.ini"
    # print(type(os.altsep))
    # file = ".."+os.altsep+"conf.ini"
    file1 = ".."
    file2 = "conf.ini"
    file=os.path.join(file1,file2)
    print(file)
    cf.read(file)
    URL=cf.get("parameter","url")
    # print(cf.get("parameter","url"))
    def getHeader(self):
        header={
            "content-type":"application/x-www-form-urlencoded",
            "":"",
        }

    def postHeader(self):
        header={
            "accept":"application/json",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "content-type":"application/x-www-form-urlencoded",
            "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36",
            "cookie":"uid=CjozJl3YR6q3z7YpiNlQAg==; s_cc=true; atgregion=11010200%7C%E5%8C%97%E4%BA%AC%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%9C%9D%E5%A4%96%E8%A1%97%E9%81%93%7C11010000%7C11000000%7C110102002; cartnum=0_0-1_0; __clickidc=81804772174584888; __c_visitor=81804772174584888; __gmc=ffb8de7; __gmv=1225660401879.1574584888331; ufpd=79ff4a9ddc75e28fbd8e13238b650163fba98d42c87dffdd4865d953ca25c45ddead40723941999d0ad23c8099d049cf089b0daa0df4eb9f8af87a0d6ec9acd0|5dda4279dwZagYBdbXHB2WfmvN00PJ9VWk7pb2B1; _smt_uid=5dda423c.160a9259; s_ppv=-%2C93%2C93%2C789; s_getNewRepeat=1574584919981-Repeat; s_sq=gome-prd%3D%2526pid%253D%2525E5%25259B%2525BD%2525E7%2525BE%25258E%2525E7%252599%2525BB%2525E5%2525BD%252595%2526pidt%253D1%2526oid%253Dfunctiononclick(event)%25257BloginGome(preLogin)%25253Breturnfalse%25253B%25257D%2526oidt%253D2%2526ot%253DBUTTON; SCN=apsQrhlgqqZJ7Z5SQVFQ7mAAG5sTZf3LLXc%2BdlH3o9atuZVXUfoxsTGeKkDxnkWf4xkEhMiIgPRw65TjP7WsJjmhMOT5e0RpbtzMsEmtnYsU1MugtWydPQ%3D%3D6066d4ca62f36b0cb3be216e7d37f597; sid=72001368571; SSO_USER_ID=72001368571; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2272001368571%22%2C%22%24device_id%22%3A%2216e94d71f76146-0e7def57a3073f-1c3b6a5b-1296000-16e94d71f77893%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216e94d71f76146-0e7def57a3073f-1c3b6a5b-1296000-16e94d71f77893%22%7D; __ugk=888ee88944f847309a55e5e115b3c660; __uls=Y; __unick=%25E5%25B8%2585%25E5%25BE%2597%25E8%25A2%25AB%25E7%25A0%258D1; gpid=11000000; gcid=11010000; gdid=11010200; gtid=110102002; awaken=true; __gma=ffb8de7.1225660401879.1574584888331.1574584888331.1574592327455.2; __gmb=ffb8de7.1.1225660401879|2.1574592327455; __gmz=ffb8de7|-|-|direct|-|-|-|1225660401879.1574584888331|dc-2|1574592327456; route=da14b3031939440e8c58e63889ebe32d"
        }
        return header

    sjson=cf.get("parameter","ajson")
    print(sjson)





