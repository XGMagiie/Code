"""
    992.K个不同整数的子数组  f(nums, =k) = f(nums, <=k) - f(nums, <=k-1)
    https://leetcode.cn/problems/subarrays-with-k-different-integers/
"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def f(c) -> int:  # 数字种类不超过 c 的数组个数
            cnt = defaultdict(int)
            ans, val, left = 0, 0, 0
            for right, num in enumerate(nums):
                if cnt[num] == 0:
                    val += 1  # 种类个数加 1
                cnt[num] += 1
                while val > c:  # 超过 c 个种类时 左边界右移
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        val -= 1
                    left += 1
                ans += right - left + 1  # 不超过 c 的数组个数
            return ans

        return f(k) - f(k - 1)
