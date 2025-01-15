"""
    862.和至少为K的最短子数组  单调队列  前缀和  因为存在负数所以和普通的滑动窗口不同
    https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/
"""
from collections import deque
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()  # 里面存放的是前缀和  从小到大
        s = list(accumulate(nums, initial=0))  # 前缀和
        ans = inf
        for i in range(n + 1):
            while q and s[i] - s[q[0]] >= k:  # 当前前缀和达标
                # [q[0] + 1..i] = [1..i] - [1..q[0]]
                ans = min(ans, i - q.popleft())  # 记录答案
            while q and s[i] <= s[q[-1]]:
                # 相等 当前的解会更优  大于 如果减去当前值会更小
                q.pop()
            q.append(i)  # 放入当前下标
        return ans if ans != inf else -1
