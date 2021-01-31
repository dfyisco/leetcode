# -*- coding: utf-8 -*-
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

"""

class Solution:
    #将每个字母对应一个质数，这样可以使得字母相同的字符串的各个字母的乘积唯一
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    def special_v(self, Str):
        p = 1
        for i in Str:
            p *= Solution.prime[ord(i)-97]
        return p

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        result = {}

        for i in range(len(strs)):
            value = self.special_v(strs[i])
            if value not in result:
                result[value] = [strs[i]]
            else:
                result[value].append(strs[i])
        return list(result.values())