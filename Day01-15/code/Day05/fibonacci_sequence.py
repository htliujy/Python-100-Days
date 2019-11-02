#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fibonacci_sequence.py
@Time    :   2019/11/02 14:09:29
@Author  :   Jack Lau 
@Version :   1.0
@Contact :   sysu.liujy@hotmail.com
@License :   
@Desc    :   斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为兔子数列。斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
'''
# here put the import lib
fib_i = 0
fib_j = 1
fib = []
for i in range(2, 21):
    fib.append(fib_j)
    fib_i, fib_j = fib_j, fib_j+fib_i
print(fib)