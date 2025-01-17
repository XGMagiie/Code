"""
    1139.最大的以1为边界的正方形  二维前缀和 枚举边长  => 总和 - 内部和 == 边长总和
    https://leetcode.cn/problems/largest-1-bordered-square/
"""
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i - 1][j - 1]

        def query(a: int, b: int, c: int, d: int) -> int:
            return s[c][d] - s[c][b - 1] - s[a - 1][d] + s[a - 1][b - 1]

        if query(1, 1, m, n) == 0:
            return 0

        ans = 1  # 枚举边长
        for x1 in range(1, m + 1):
            for y1 in range(1, n + 1):
                x2, y2, k = x1 + ans, y1 + ans, ans + 1
                while x2 <= m and y2 <= n:
                    if (query(x1, y1, x2, y2) - query(x1 + 1, y1 + 1, x2 - 1, y2 - 1)) == (k - 1) << 2:
                        ans = k
                    x2, y2, k = x2 + 1, y2 + 1, k + 1
        return ans * ans
