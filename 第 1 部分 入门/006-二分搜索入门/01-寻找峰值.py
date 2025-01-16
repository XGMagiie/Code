"""
    162.寻找峰值  非有序数组上二分搜索
    https://leetcode.cn/problems/find-peak-element/description/
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:  # 答案在 mid 左侧
                high = mid - 1
            elif mid < n - 1 and nums[mid] < nums[mid + 1]:   # 答案在 mid 右侧
                low = mid + 1
            else:
                return mid
