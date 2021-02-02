# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:03:48 2021

@author: ThinkPad
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = list()
        queens = [-1]*n #初始化皇后的位置
        col = set()
        diag1 = set()
        diag2 = set()
        def backtrack(row):
            if row == n: # 当找到所有皇后的位置（符合条件）， 将结果添加到solutions列表中
                board = generateboard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in col or row - i in diag1 or row + i in diag2: 
                        #如果该列或该单元格所在两条对角线上已经有皇后，那么继续判断该列的下一格
                        continue
                    queens[row] = i # 记录第i行皇后的位置（即列号）
                    col.add(i)
                    diag1.add(row - i)
                    diag2.add(row + i)
                    backtrack(row + 1) # 回溯算法， 寻找下一行皇后的位置
                    col.remove(i)
                    diag1.remove(row - i)
                    diag2.remove(row + i)
        rows = "."*n
        def generateboard():
            board = []
            for i in range(n):
                line = list(rows)
                line[queens[i]] = 'Q' #将对应位置的 '.' 换为 'Q'
                line = ''.join(line)
                board.append(line)
            return board
        backtrack(0)
        return solutions