"""
    875.爱吃香蕉的珂珂  bisect_left
    https://leetcode.cn/problems/koko-eating-bananas/
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        # 第一个大于等于的值 bisect_left
        while low < high:
            mid = low + (high - low) // 2
            if sum((pile + mid - 1) // mid for pile in piles) <= h:
                high = mid  # 可能是答案
            else:  # 不可能是答案
                low = mid + 1
        return low
