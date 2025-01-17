"""
    287.寻找重复数  快慢指针  因为里面存在一个环
    https://leetcode.cn/problems/find-the-duplicate-number/description/
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n 个顶点 n 条边 必定有环 且下标 0 为入口
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0  # 相遇后重新走
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
