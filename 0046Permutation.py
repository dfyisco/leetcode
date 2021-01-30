# -*- coding: utf-8 -*-
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        def backtrack(LIST, nextnums):
            if not nextnums:
                result.append(LIST)
            else:
                for i in range(len(nextnums)):
                    backtrack(LIST + [nextnums[i]], nextnums[:i] + nextnums[i+1:])
        backtrack([], nums)
        return result