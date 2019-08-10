#!/usr/bin/evn python3
# -*- coding:utf-8 -*

def dictget(dict1,obj,default=None):
 for k,v in dict1.items():
  if k == obj:
   print(v)
  else:
   if type(v) is dict:
    re=dictget(v,obj)
    if re is not default:
     print(re)

dict1={'result': 0, 'data': {'nickname': '慕粉3418961', 'mp': '7,240', 'img': 'http:\\/\\/img4.mukewang.com\\/575c43410001f87d04190419-100-100.jpg', 'uid': '3418961', 'credit': '4', 'last_learning': {'course_name': '接口测试基础之入门篇', 'last_chapter_media': '4-1', 'media_name': '接口测试工具-python-get接口实战', 'course_id': '738', 'media_id': '13104', 'url': '\\/\\/www.imooc.com\\/video\\/13104'}, 'user_type': '1', 'coupons': '0'}, 'msg': '成功'}
dictget(dict1,"media_name")