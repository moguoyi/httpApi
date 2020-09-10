from httpApi.studyTest.operateJson import OperetionJson
from httpApi.commons.operateConfig import OperateConfig
address="/Users/moguoyi/pyStudy/httpApi/file/json/gome_data.json"

print(OperetionJson().read_data())
print(OperetionJson("/Users/moguoyi/pyStudy/httpApi/file/json/gome_data.json").read_data())
print(OperateConfig().read_value("parameter","url"))
print(OperateConfig("/Users/moguoyi/pyStudy/httpApi/file/conf.ini").read_value("parameter","url"))