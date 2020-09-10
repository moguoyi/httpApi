#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020-07-12 15:15
# @Author  : moguoyi
# @Email   : moguoyi@163.com
# @File    : bubbling.py
# @Software: PyCharm


def bubbling(nums):
    for i in range(len(nums), 0, -1):
        flag = 0
        for j in range(i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = 1
        if not flag:
            break
    print(nums)

nums1 = [9, 4, 2, 7, 5]
bubbling(nums1)


