"""
    2208.将数组和减半的最少操作次数  贪心
    https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/description/
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq, sum1 = [], 0
        for num in nums:
            heappush(pq, -num)
            sum1 += num
        cnt, sum2 = 0, 0
        while sum2 * 2 < sum1:
            x = -heappop(pq) / 2
            sum2 += x
            heappush(pq, -x)
            cnt += 1
        return cnt
