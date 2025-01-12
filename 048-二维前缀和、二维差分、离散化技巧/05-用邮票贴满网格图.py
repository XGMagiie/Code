"""
    2312.用邮票贴满网格图   二维差分 + 二维前缀和
    https://leetcode.cn/problems/stamping-the-grid/description/
"""
from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i - 1][j - 1]

        def query(a: int, b: int, c: int, d: int) -> int:
            return s[c][d] - s[c][b - 1] - s[a - 1][d] + s[a - 1][b - 1]

        def update(a: int, b: int, c: int, d: int) -> None:
            diff[a][b] += 1
            diff[c + 1][b] -= 1
            diff[a][d + 1] -= 1
            diff[c + 1][d + 1] += 1

        # 二维差分
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for a in range(1, m + 1):
            for b in range(1, n + 1):
                c, d = a + stampHeight - 1, b + stampWidth - 1
                if c <= m and d <= n and query(a, b, c, d) == 0:  # 可以贴邮票
                    update(a, b, c, d)
        # 二维前缀和
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                if diff[i][j] == 0 and grid[i - 1][j - 1] == 0:  # 当前位置没有贴邮票且原本是 0
                    return False
        return True
