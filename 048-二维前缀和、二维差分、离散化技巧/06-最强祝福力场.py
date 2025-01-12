"""
    LCP74.最强祝福力场    离散化
    https://leetcode.cn/problems/xepqZ5/description/
"""
from typing import List


class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        from bisect import bisect_left
        # 离散化
        idx, idy = set(), set()
        for x, y, side in forceField:
            idx.add((x << 1) - side)
            idx.add((x << 1) + side)
            idy.add((y << 1) - side)
            idy.add((y << 1) + side)
        idx = list(sorted(idx))
        idy = list(sorted(idy))

        def update(a: int, b: int, c: int, d: int) -> None:
            diff[a][b] += 1
            diff[c + 1][b] -= 1
            diff[a][d + 1] -= 1
            diff[c + 1][d + 1] += 1

        # 二维差分
        n, m = len(idx), len(idy)
        diff = [[0] * (m + 2) for _ in range(n + 2)]
        for x, y, side in forceField:
            a = bisect_left(idx, (x << 1) - side) + 1
            b = bisect_left(idy, (y << 1) - side) + 1
            c = bisect_left(idx, (x << 1) + side) + 1
            d = bisect_left(idy, (y << 1) + side) + 1
            update(a, b, c, d)

        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                ans = max(ans, diff[i][j])
        return ans
