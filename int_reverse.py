# -*- coding: utf-8 -*-
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution:
    def reverse(self, x: int) -> int:
        r_x = 0
        temp = 0
        s = x
        if x < 0:
            s = s - 2*s
        while s != 0:
            r_x = temp + s%10
            temp = r_x*10
            s = (s - s%10)//10
        if r_x > 2**31 - 1 or r_x < -2**31:
            return 0 
        if x >= 0:
            return r_x
        if x < 0:
            return -r_x