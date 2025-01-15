"""
    1499.满足不等式的最大值  普通滑动窗口 + 算式变型
    https://leetcode.cn/problems/max-value-of-equation/description/
"""
from cmath import inf
from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # yi + yj + |xi - xj| = yj + xj + yi - xi
        # 将 yi - xi 放入(大 -> 小)窗口中
        q = deque()  # 从小到大
        ans = -inf
        for x, y in points:
            while q and x - q[0][0] > k:
                q.popleft()  # 去除左边越界的
            if q:
                ans = max(ans, x + y + q[0][1])
            while q and y - x > q[-1][1]:
                q.pop()  # 淘汰小于 当前 的 y - x
            q.append((x, y - x))
        return ans
