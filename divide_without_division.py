# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 23:35:03 2021

@author: ThinkPad
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