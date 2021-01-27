# -*- coding: utf-8 -*-
"""

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        l, r = 0, len(height) - 1
        V = 0
        max_left, max_right = height[0], height[len(height)-1]
        while l <= r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            if max_left < max_right:
                V += max_left - height[l]
                l += 1
            else:
                V += max_right - height[r]
                r -= 1
        return V