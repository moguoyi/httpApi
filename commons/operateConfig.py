import os
import configparser


class OperateConfig:

    def __init__(self, address=None):
        if address == None:
            # self.address = os.path.join("..","conf.ini")
            self.address = os.path.join(os.path.dirname(
                           os.path.dirname(__file__)), "conf.ini")
        else:
            self.address = address
        self.config = self.get_config()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.address)
        return config

    def read_value(self, name, value):
        return self.config.get(name, value)


if __name__ == "__main__":
    address = "/Users/moguoyi/pyStudy/httpApi/file/conf.ini"
    print(OperateConfig().read_value("parameter", "url"))
    print(OperateConfig(address).read_value("parameter", "url"))
    print(os.path.join(os.path.split(os.path.realpath(__file__))[0], "conf.ini"))
    print(os.path.dirname(__file__))
    print(os.path.dirname(os.path.dirname(__file__)))






