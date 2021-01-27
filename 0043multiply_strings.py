# -*- coding: utf-8 -*-
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        SUM = 0
        n1 = len(num1)
        n2 = len(num2)
        for i in range(n1):
            for j in range(n2):
                SUM += ((ord(num1[i]) - 48)*10**(n1-i-1))*((ord(num2[j]) - 48)*10**(n2-j-1))
        return str(SUM)
