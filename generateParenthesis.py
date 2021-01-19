# -*- coding: utf-8 -*-
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_list = []
        total_list.append([None])
        total_list.append(["()"])
        for i in range(2, n+1):
            l = []
            for j in range(i):
                list1 = total_list[j]
                list2 = total_list[i-1-j]
                for k1 in list1:
                    for k2 in list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        element = "(" + k1 + ")" + k2
                        l.append(element)
            total_list.append(l)
        return total_list[n]