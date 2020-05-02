import os
import configparser
import json

class OperateConfig:

    def __init__(self,address = None):

        if address == None:
            self.address = os.path.join("..","conf.ini")
        else:
            self.address = address
        self.config = self.get_config()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.address)
        return config

    def read_value(self,name,value):
        return self.config.get(name,value)

# if __name__ == "__main__":
#     address = "/Users/moguoyi/pyStudy/httpApi/file/conf.ini"
#     print(OperateConfig().read_value("parameter","url"))
#     print(OperateConfig(address).read_value("parameter","url"))




