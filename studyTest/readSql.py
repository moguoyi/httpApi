#coding:utf-8
import os

# path = os.getcwd()
# print(path)
with open(r'../file/testSql/test.sql',encoding='utf-8',mode='r') as f:
    # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
    sql_list = f.read().split(';')[:-1]
    for x in sql_list:
        # 判断包含空行的
        if '\n' in x:
            # 替换空行为1个空格
            x = x.replace('\n', '')

        # sql语句添加分号结尾
        sql_item = x+';'
        print(sql_item)