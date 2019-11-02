#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   buy_chikens.py
@Time    :   2019/11/02 14:00:29
@Author  :   Jack Lau 
@Version :   1.0
@Contact :   sysu.liujy@hotmail.com
@License :   
@Desc    :   None
    百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
'''
# here put the import lib
# 母鸡: x
# 公鸡: y
# 小鸡: z
for x in range(0,21):
    for y in range (0,34):
        z = 100-x-y
        if 5 * x + 3 * y + z / 3 == 100:
            print("公鸡{}只，母鸡{}只，小鸡{}只".format(x,y,z))
