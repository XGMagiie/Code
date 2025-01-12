"""
    803.打砖块
    https://leetcode.cn/problems/bricks-falling-when-hit/description/
"""
from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # 1 炮弹打的地方 -1
        for i, j in hits:
            grid[i][j] -= 1

        # 2 从天花板进行填充
        def dfs(i: int, j: int) -> int:
            # 统计 1 的个数
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] != 1:
                return 0
            grid[i][j] = 2  # 去掉
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for j in range(n):
            dfs(0, j)

        # 3 从后往前处理数据
        def worth(i: int, j: int) -> bool:
            # 第一行 或 周围是否存在 2
            return i == 0 or (i > 0 and grid[i - 1][j] == 2) or (i < m - 1 and grid[i + 1][j] == 2) \
                or (j > 0 and grid[i][j - 1] == 2) or (j < n - 1 and grid[i][j + 1] == 2)

        ans = [0] * len(hits)
        for _ in range(len(hits) - 1, -1, -1):
            i, j = hits[_]
            grid[i][j] += 1
            if grid[i][j] == 1 and worth(i, j):
                ans[_] = dfs(i, j) - 1
        return ans
