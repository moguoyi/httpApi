#写文件
import xlwt;
#读文件
import xlrd;
#若要对excel文件进行修改必须！要引入这个工具模块，其中含有复制和修改功能---------注意引入方式
import xlutils;
# from xltuils.copy import copy;


import unittest;
import requests;
#使用写文件模式打开文件
open_workbook=xlrd.open_workbook('/Users/moguoyi/mo1.xlsx');
#最终返回的是文件类型
print(open_workbook);
# 打印该文件下，对应数据表的行数
table=open_workbook.sheets()[0]
# print(open_workbook.sheet_names())
# print(open_workbook.sheet_by_name('工作表1').nrows);
# table =open_workbook.sheet_by_index(sheet_indx)) #通过索引顺序获
# table=open_workbook.sheet_by_index(sheet_indx)
print(table.nrows);
print(table.cell_value(1,1))


# #循环打印出所有数据,并分别保存在list中
# #编号
# listkey=[];
# #测试地址
# listurl=[];
# #提交方式
# listtype=[];
# #参数1
# listcanshu1=[];
# #参数2
# listcanshu2=[];
# #预期结果
# listyuqi=[];
# #实际结果
# listresult=[];
# #在unitest框架中，通过调用参数，执行用例，将实际结果比对预期结果是否一致，若一致，则通过，否则用例失败，并将实际结果写入excel中（写入代码后文将写到）
# for item_row in range(1,open_workbook.sheet_by_name('mytest').nrows):
#     #获取用例编号
#     listkey.append(open_workbook.sheet_by_name('mytest').cell(item_row,0).value);
#     # 获取参数1
#     listcanshu1.append(open_workbook.sheet_by_name('mytest').cell(item_row, 1).value);
#     # 获
