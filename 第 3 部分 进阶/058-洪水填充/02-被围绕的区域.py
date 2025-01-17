"""
    130.被围绕的区域  从外围向内标记
    https://leetcode.cn/problems/surrounded-regions/description/
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i == m or j < 0 or j == n or board[i][j] != 'O':
                return
            board[i][j] = '#'  # 去掉
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 第一行和最后一行
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
        # 第一列和最后一列
        for i in range(1, m - 1):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        # 更新数据
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'  # 恢复
