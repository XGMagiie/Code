"""
    136.只出现一次的数字
    https://leetcode.cn/problems/single-number/description/
"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
