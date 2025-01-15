"""
    739.每日温度  找右边第一个大于当前值的下标
    https://leetcode.cn/problems/daily-temperatures/description/
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = list()  # 单调栈  从大到小
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
