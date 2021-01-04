# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:39:38 2021

@author: ThinkPad
"""

#给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

#进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) >= len(nums2):
            for i in nums2:
                nums1.append(i)
            L = sorted(nums1)
        elif len(nums2) > len(nums1):
            for i in nums1:
                nums2.append(i)
            L = sorted(nums2)
        if len(L)%2 == 1:
            medium = L[len(L)//2]
        elif len(L)%2 == 0:
            medium = (L[len(L)//2] + L[len(L)//2 - 1])/2
        return medium