#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   narcissistic_number.py
@Time    :   2019/11/02 13:42:55
@Author  :   Jack Lau 
@Version :   1.0
@Contact :   sysu.liujy@hotmail.com
@License :   
@Desc    :   水仙花数
    水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：
1^3+3^3+5^3 = 153
'''
# here put the import lib
num = 0
for i in range (100,1000):
    ones_place = i%10
    tens_place = i//10%10
    hundreds_place = i//100
    if i == ones_place**3 + tens_place**3 + hundreds_place**3:
        print("%d is narcissistic number!"%i)
        num += 1
print("There is {} narcissistic number at all.".format(num))
