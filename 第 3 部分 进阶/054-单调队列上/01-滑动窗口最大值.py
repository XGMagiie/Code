"""
    239.滑动窗口最大值
    https://leetcode.cn/problems/sliding-window-maximum/description/
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = deque()
        ans = list()
        for i in range(len(nums)):
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
            Q.append(i)
            while Q and Q[0] + k <= i:
                Q.popleft()
            if i >= k - 1:
                ans.append(nums[Q[0]])
        return ans
