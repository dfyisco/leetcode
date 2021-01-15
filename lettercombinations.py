# -*- coding: utf-8 -*-
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
"""

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        num_dict = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'], 
                    '5':['j','k','l'], 
                    '6':['m','n','o'], 
                    '7':['p','q','r','s'], 
                    '8':['t','u','v'], 
                    '9':['w','x','y','z']
                    }
        result = []
        def backtrack(strs, nextdigit):
            if len(nextdigit) == 0:
                result.append(strs)
            else:
                for letter in num_dict[nextdigit[0]]:
                    backtrack(strs + letter, nextdigit[1:])

        backtrack("", digits)
        return result