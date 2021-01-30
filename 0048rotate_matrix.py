# -*- coding: utf-8 -*-
"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range((n+1)//2):
            for i in range(n-2*j-1):
                matrix[j][j+i], matrix[j+i][n-1-j], matrix[n-1-j][n-1-j-i], matrix[n-1-j-i][j] = matrix[n-1-j-i][j], matrix[j][j+i], matrix[j+i][n-1-j], matrix[n-1-j][n-1-j-i]