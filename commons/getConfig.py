import os
import configparser

class GetConfig:

    def read_value(self,name,value,address = None):
        if address == None:
            address = os.path.join("..","conf.ini")
        config = configparser.ConfigParser()
        config.read(address)

        return config.get(name,value)

if __name__ == "__main__":
    GetConfig = GetConfig()
    print(GetConfig.read_value("parameter","url"))
    print(GetConfig.read_value("parameter", "url", "/Users/moguoyi/pyStudy/httpApi/file/conf.ini"))