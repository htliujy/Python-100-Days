#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   perfect_num.py
@Time    :   2019/11/02 14:20:14
@Author  :   Jack Lau 
@Version :   1.0
@Contact :   sysu.liujy@hotmail.com
@License :   
@Desc    :   找出10000以内的完美数
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（6=1+2+3）和28（28=1+2+4+7+14）就是完美数。
'''
# here put the import lib
"""
代码问题：
    1、没有打印出：1，但问题是，1是答案吗？？
    2、运算慢
    别人的代码用这样的语句解决的，算法写起来更复杂一点，但是快。
        for factor in range(1, int(math.sqrt(num)) + 1):
"""
perfect_num =[]
for i in range(1,10000):
    sigma = 0
    for factor in range(1,i):
        if i%factor ==0:
            sigma += factor
    if sigma == i:
        perfect_num.append(i)

print("perfect number in range 10000:{}".format(perfect_num))