#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020-07-07 01:13
# @Author  : moguoyi
# @Email   : moguoyi@163.com
# @File    : test_one.py
# @Software: PyCharm


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_fail():
    assert (1, 2, 3) == (3, 2, 3)