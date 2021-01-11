# -*- coding: utf-8 -*-
"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        len_s = m + 1
        len_p = n + 1
        result = [[False]*len_s for i in range(len_p)]

        result[0][0] = True
        if len_s == len_p == 1:
            return True
        if len_p == 1:
            return False
        if p[0] == "*":
            return False
        
        s = '_' + s
        p = '_' + p


        for i in range(1, len_p):

            if p[i] == '*':
                result[i][0] = result[i-2][0]
            
            for j in range(1, len_s):
                if p[i] != '*':
                    result[i][j] = result[i-1][j-1] & self.match(p[i],s[j])
                else:
                    result[i][j] = result[i-2][j] | result[i-1][j] | result[i][j-1] & self.match(p[i-1],s[j])

        return result[-1][-1]

    def match(self, i, j):
        if i == j or i == '.':
            return True
        else:
            return False