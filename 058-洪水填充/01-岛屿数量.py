"""
    200.岛屿数量  dfs(i - 1, j) dfs(i + 1, j) dfs(i, j - 1) dfs(i, j + 1)
    https://leetcode.cn/problems/number-of-islands/description/
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # 去掉
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans
