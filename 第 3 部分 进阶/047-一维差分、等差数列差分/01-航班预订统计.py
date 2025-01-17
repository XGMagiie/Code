"""
    1109.航班预订统计  一维差分  a[l] += x  a[r + 1] -= x
    https://leetcode.cn/problems/corporate-flight-bookings/description/
"""
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a = [0] * (n + 2)
        for l, r, x in bookings:
            a[l] += x
            a[r + 1] -= x
        ans = [0] * n
        cur = 0
        for i in range(1, n + 1):
            cur += a[i]
            ans[i - 1] = cur
        return ans
