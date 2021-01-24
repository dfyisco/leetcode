# -*- coding: utf-8 -*-
"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-sudoku
"""

class Solution:
    def isValidSudoku(self, board) -> bool:
        # 生成状态存储列表
        row = [[0]*9 for k in range(9)]
        col = [[0]*9 for k in range(9)]
        box = [[0]*9 for k in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': # 遇到空格跳过
                    continue
                num = ord(board[i][j]) - ord('0') # 将字符型变量转化为整型
                if row[i][num-1] != 0 or col[j][num-1] != 0 or box[j//3 + (i//3)*3][num-1] != 0: 
                    # 如果在该行该列或该九宫格中存在对应的数字 num， 则返回false
                    return False
                # 记录数字num已经在该行该列和该九宫格中出现过
                row[i][num-1] = 1
                col[j][num-1] = 1
                box[j//3 + (i//3)*3][num-1] = 1
        return True
