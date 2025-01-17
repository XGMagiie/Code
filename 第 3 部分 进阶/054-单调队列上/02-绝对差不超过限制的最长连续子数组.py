"""
    1438.绝对差不超过限制的最长连续子数组  维持两个单调队列
    https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
"""
from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        Max, Min = deque(), deque()
        left, ans = 0, 0
        for right in range(len(nums)):
            while Max and Max[-1] < nums[right]:
                Max.pop()
            while Min and Min[-1] > nums[right]:
                Min.pop()
            Max.append(nums[right]); Min.append(nums[right])
            while Max and Min and Max[0] - Min[0] > limit:
                if Max[0] == nums[left]:
                    Max.popleft()
                if Min[0] == nums[left]:
                    Min.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans
