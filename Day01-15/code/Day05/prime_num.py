#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   prime_num.py
@Time    :   2019/11/02 14:34:24
@Author  :   Jack Lau 
@Version :   1.0
@Contact :   sysu.liujy@hotmail.com
@License :   
@Desc    :   输出100以内所有的素数。

'''
# here put the import lib
import math

prime = []
for i in range(2,100):
    is_prime = True
    for j in range (2,int(math.sqrt(i))+1):
        #there has a bug, because 2 is not been checked to be a prime number.
        if i%j ==0:
            is_prime = False
            break;
    if is_prime == True:
        prime.append(i)
print("prime number in range 100:{}".format(prime))