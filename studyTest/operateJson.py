import json

class OperetionJson:
    def __init__(self,address = None):
        if address == None:
            self.address = "../file/moyi.json"
        else:
            self.address=address
        self.data=self.read_data()

    def read_data(self):
        with open(self.address) as fp:
            data=json.load(fp)
            return data

    def get_data(self,id):
        return self.data[id]



if __name__=="__main__":
    address="/Users/moguoyi/pyStudy/httpApi/file/json/gome_data.json"

    print(OperetionJson(address).read_data())
    print(OperetionJson().read_data())
