"""
    922.按奇偶排序数组II
    https://leetcode.cn/problems/sort-array-by-parity-ii/description/
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even, odd = 0, 1
        while even < n and odd < n:
            if nums[n - 1] & 1:  # 最后一位是奇数
                nums[odd], nums[n - 1] = nums[n - 1], nums[odd]
                odd += 2
            else:  # 最后一位是偶数
                nums[even], nums[n - 1] = nums[n - 1], nums[even]
                even += 2
        return nums
