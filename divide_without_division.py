# -*- coding: utf-8 -*-
"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1 # 设置上下限范围
        flag = 1 
        # 处理除数与被除数的符号问题
        if dividend < 0:
            flag = -flag
            dividend = - dividend
        if divisor < 0:
            flag = -flag
            divisor = -divisor
        
        res = 0 #设置结果 result
        # 以二进制法搜索
        while dividend >= divisor:  # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
            cur = divisor
            m = 1
            while cur + cur < dividend:
                cur += cur
                m += m 
            dividend -= cur
            res += m 
        res = flag*res #恢复符号的问题

        if res > MAX:
            return MAX
        elif res < MIN:
            return MIN
        else: return res
