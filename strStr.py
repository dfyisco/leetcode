# -*- coding: utf-8 -*-
"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0 
        if len(haystack) == 0:
            return -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            else:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1