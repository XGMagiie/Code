"""
    200.岛屿数量  集合个数
    https://leetcode.cn/problems/number-of-islands/description/
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        father = [-1] * (n * m)
        sets = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':  # 水
                    continue
                father[i * m + j] = i * m + j
                sets += 1

        def find(a: int) -> int:
            if a != father[a]:
                father[a] = find(father[a])
            return father[a]

        def union(a: int, b: int) -> None:
            fa, fb = find(a), find(b)
            if fa == fb:
                return
            father[fa] = fb
            nonlocal sets
            sets -= 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':  # 水
                    continue
                if j > 0 and grid[i][j - 1] == '1':
                    union(i * m + j, i * m + j - 1)
                if i > 0 and grid[i - 1][j] == '1':
                    union(i * m + j, (i - 1) * m + j)
        return sets
