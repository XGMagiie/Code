"""
    260.只出现一次的数字III
    https://leetcode.cn/problems/single-number-iii/description/
"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = reduce(lambda x, y: x ^ y, nums)
        lsb = xorsum & (-xorsum)  # 提取右侧的 1
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        return [type1, type2]
