#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
import time
import HTMLTestRunner
import HTMLTestRunnerCN
from  httpApi.defTest import wrapperCalculation

class TestCal(unittest.TestCase):
    ad=wrapperCalculation.Calculation()
    def setUp(self):
        ad = wrapperCalculation.Calculation()
        print("-------------开始测试-----------")

    def test_add(self):
        self.assertEqual(3,self.ad.add(1,3))
        self.assertEqual(10,self.ad.add(9,9))
    def test_sub(self):
        self.assertEqual(9,self.ad.sub(2,4))

    def test_mul(self):
        self.assertEqual(100,self.ad.mul(10,10))

    def test_div(self):
        self.assertEqual(9,self.ad.div(9,1))
        self.assertEqual(99, self.ad.div(99, 1))
    def tearDown(self):
        print("--------测试结束------")


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    now = time.strftime('%Y-%m%d %H%M%S')
    print(now)
    filename = '/Users/moguoyi/pyStudy/httpApi/report/ ' + now + 'result.html'
    fp = open(filename, 'wb')
    s = unittest.TestSuite()  # 实例化
    s.addTest(TestCal("test_sub"))
    s.addTest(TestCal("test_add"))
    s.addTest(TestCal("test_mul"))# 加载用例
    s.addTest(TestCal("test_div"))
    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # 8.3.2执行测试用例
    # 8.3.2.1实例化TextTestRunner类
    # runner = unittest.TextTestRunner()

    # runner = HTMLTestRunner.HTMLTestRunner(fp, verbosity=2, title='xxx项目测试报告', description='详细测试结果',tester='测试人员姓名')
    # runner.run(s)

    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='xx项目测试报告',
        description='详细测试用例结果',
        tester='测试人员姓名'
    )
    runner.run(s)
    fp.close()
    # unittest.main()