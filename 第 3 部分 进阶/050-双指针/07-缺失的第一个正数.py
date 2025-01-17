"""
    41.缺失的第一个正数  非常难以想到
    https://leetcode.cn/problems/first-missing-positive/description/
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [0 : l - 1] 已经放好了 [1 ... l]
        # [r : ] 存放无用的数据
        l, r = 0, len(nums)
        while l < r:
            # 假定[l : r] 能凑出 [1 ... r]
            if nums[l] == l + 1:
                l += 1
            elif nums[l] < l + 1 or nums[l] > r:  # 不在范围内此时 nums[l] 无用
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] == nums[nums[l] - 1]:  # nums[l] 在 [l .. r] 中重复不要
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:  # 此时只需交换 l 和 nums[l] - 1 的值即可
                nums[nums[l] - 1], nums[l] = nums[l], nums[nums[l] - 1]
        return l + 1
