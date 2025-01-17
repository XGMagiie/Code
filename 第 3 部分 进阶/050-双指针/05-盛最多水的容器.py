"""
    11.盛最多水的容器  移动高度较小的一遍 贪心证明较难
    https://leetcode.cn/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans, left, right = 0, 0, n - 1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:  # 移动左指针
                left += 1
            else:  # 移动右指针
                right -= 1
        return ans
