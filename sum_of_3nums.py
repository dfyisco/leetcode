# -*- coding: utf-8 -*-
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


"""

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        sort_nums = sorted(nums)
        result = []
        length = len(nums)
        for i in range(length):
            if sort_nums[i] > 0:
                return result
            if i > 0 and sort_nums[i] == sort_nums[i-1]:
                continue
            L = i + 1
            R = length - 1
            while L < R:
                if sort_nums[i] + sort_nums[L] + sort_nums[R] == 0:
                    result.append([sort_nums[i],sort_nums[L],sort_nums[R]])
                    while L < R and sort_nums[L] == sort_nums[L+1]:
                        L += 1
                    while L < R and sort_nums[R] == sort_nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif sort_nums[i] + sort_nums[L] + sort_nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return result