#！coding:utf-8
import json

class Mjson(object):
    adict = {"xiaoqiangk": "xiaoqiangv", "xiaofeik": "xiaofeiv",
             "xiaofeis": {"xiaofeifk": "xiaofeifv",
             "xiaofeimk": {"xiaoqik": "xiaoqiv","xiaogou": {
             "xiaolei": "xiaolei"}}},
             "xiaoer": {"xiaoyuk": "xiaoyuv"}}
    def hjson(selt,json1,key,i=0):
        if isinstance(json1,dict):
            for item in json1:
                if isinstance(json1[item],dict):
                    if item==key:
                      print("****"*i+"%s : %s"%(item,json1[item]))
                    selt.hjson(json1[item],key,i=i+1)
                else:
                    if item==key:
                     print("{} : {}".format(item,json1[item]))
                    # print("****" * i + "%s : %s" % (item, json1[item]))
        else:
            print("json1  is not josn object!")


if __name__=="__main__":
    c=Mjson()
    c.hjson(c.adict,"xiaoyuk",0)

