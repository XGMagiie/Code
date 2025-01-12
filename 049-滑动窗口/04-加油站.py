"""
    134.加油站  余量数组 = 油量数组 gas - 路程数组 cost
    https://leetcode.cn/problems/gas-station/description/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        left, right = 0, 0
        while left < n:  # 枚举左端点
            s = 0  # 记录油耗
            while s + gas[right % n] - cost[right % n] >= 0:  # 可以继续走
                if right - left + 1 == n:  # 满足条件
                    return left
                s += gas[right % n] - cost[right % n]
                right += 1
            left = right + 1  # 贪心
            right = left
        return -1
