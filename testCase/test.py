#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 首先我们导入 相关的包 一个测试需要用来发送请求的  requests
# 还有就是我么的测试框架包   unittest
import requests
import unittest
# 新建一个测试类
class Test_01(unittest.TestCase):
    # 新建测试方法
    def test_gs(self):
        # 声明一个变量   给其赋值  一个地址
        url='https://blog.csdn.net/qq_38318622'
        # 声明一个变量  拿到我们请求返回的值  这里我们使用了 text方法将请求返回的网页上的内容全部转换成字符
        response=requests.get(url)
        result=response.text
        result1=response.status_code
        # print(response)
        # 进行检查 返回的字符中是否包含 Neon
        if(result1==200):
                    print(result1)
                    print('Neon' in result)
        else:
            print("网络失败，响应码:{}".format(result1))


# 执行测试
if __name__== '__main__':
    unittest.main()
