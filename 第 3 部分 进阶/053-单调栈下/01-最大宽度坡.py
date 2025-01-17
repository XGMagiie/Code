"""
    962.最大宽度坡  单调栈内存放左边端点
    https://leetcode.cn/problems/maximum-width-ramp/description/
"""
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        st = list()  # 单调栈
        for i in range(n):
            if not st or nums[st[-1]] > nums[i]:
                st.append(i)
        ans = 0
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                ans = max(ans, i - st.pop())
        return ans
