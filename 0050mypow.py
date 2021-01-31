# -*- coding: utf-8 -*-
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n
        temp = self.myPow(x, n//2)

        if n%2 == 0:
            return temp*temp
        return temp*temp*x #对于奇数，需要乘一个额外的x