import configparser

class ConfigParsers(object):
    cf = configparser.ConfigParser()
    file="/Users/moguoyi/pyStudy/httpApi/conf.ini"
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
            "accept":"application/json, text/javascript, */*; q=0.01",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "content-type":"application/x-www-form-urlencoded",
            "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
            "cookie":""
        }
    sjson=cf.get("parameter","ajson")
    # print(sjson)





