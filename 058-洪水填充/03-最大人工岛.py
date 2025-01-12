"""
    827.最大人工岛  染色分类  枚举统计
    https://leetcode.cn/problems/making-a-large-island/description/
"""
from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(i: int, j: int, color: int) -> int:
            if i < 0 or i == n or j < 0 or j == n or grid[i][j] != 1:
                return 0
            grid[i][j] = color  # 染色
            return 1 + dfs(i - 1, j, color) + dfs(i + 1, j, color) + \
                dfs(i, j - 1, color) + dfs(i, j + 1, color)

        color = 2  # 将相连岛屿染成同一种颜色
        cnt = defaultdict(int)  # 统计相同颜色的岛屿数量
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                cnt[color] = dfs(i, j, color)
                ans = max(ans, cnt[color])
                color += 1

        # 枚举每个 0 变成 1 统计结果
        def summary(i: int, j: int) -> int:
            up = grid[i - 1][j] if i > 0 else 0
            down = grid[i + 1][j] if i < n - 1 else 0
            left = grid[i][j - 1] if j > 0 else 0
            right = grid[i][j + 1] if j < n - 1 else 0
            c = 1 + cnt[up]
            c += cnt[down] if down != up else 0
            c += cnt[left] if left != down and left != up else 0
            c += cnt[right] if right != left and right != down and right != up else 0
            return c

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans, summary(i, j))
        return ans
