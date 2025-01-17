"""
    410.分割数组的最大值  bisect_left  每一部分累加和最小
    https://leetcode.cn/problems/split-array-largest-sum/description/
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(Max: int) -> bool:
            cnt, cur = 1, 0
            for num in nums:
                if cur + num <= Max:  # 放的下
                    cur += num
                else:  # 放不下
                    cur = num
                    cnt += 1
            return cnt <= k

        low, high = max(nums), sum(nums)
        # 第一个大于等于 bisect_left
        while low < high:
            mid = low + (high - low) // 2
            if check(mid):
                high = mid  # 当前可能是答案
            else:  # 当前不是答案
                low = mid + 1
        return low
