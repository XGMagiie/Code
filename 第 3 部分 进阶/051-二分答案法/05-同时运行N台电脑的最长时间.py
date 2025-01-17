"""
    2141.同时运行N台电脑的最长时间  bisect_right  枚举时长
    https://leetcode.cn/problems/maximum-running-time-of-n-computers/description/
"""
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low, high = 0, sum(batteries) // n
        # 第一个大于的前一位 bisect_right
        while low < high:
            mid = low + (high - low + 1) // 2
            if sum(min(x, mid) for x in batteries) >= n * mid:
                low = mid  # 当前值可能是答案
            else:  # 当前值不满足
                high = mid - 1
        return low
