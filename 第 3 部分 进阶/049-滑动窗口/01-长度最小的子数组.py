"""
    209.长度最小的子数组  滑动窗口
    https://leetcode.cn/problems/minimum-size-subarray-sum/description/
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, val, ans = 0, 0, n + 1
        for right in range(n):
            val += nums[right]
            while val >= target:
                ans = min(ans, right - left + 1)
                val -= nums[left]
                left += 1
        return 0 if ans == n + 1 else ans
