import requests
from httpApi.commons.headerToParm import *

class Login(object):
    url=ConfigParsers().URL
    postHeader=ConfigParsers().postHeader()

    def gomeLogin(self):
        url=self.url+"/gmsst5Login.no"
        data={
            "loginName":"18513827507",
            "":"",
        }
