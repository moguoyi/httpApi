
from unittest.mock import MagicMock
from unittest import mock
import requests
from httpApi.studyTest.calc import Calc, Calc_Mock

class TestCalc():
    def test_1(self):
       s = Calc()
       s.add = mock.Mock(return_value=2) #当方法调用s.add()时返回 2
       print(s.add(1,2))
       assert s.add(1,2) == 2

    def test_2(self):
        s = Calc()
        s.add = MagicMock(return_value=2, side_effect=s.div)  # 当方法调用s.add()时返回 s.div()的执行结果
        print(s.add(8, 2))
        assert s.add(8, 2) == 4


if __name__=="__main__":
    mo=TestCalc()
    mo.test_1()
    mo.test_2()