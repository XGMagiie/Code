"""
    268.丢失的数字
    https://leetcode.cn/problems/missing-number/description/
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor
