"""
    493.翻转对  归并分治
    https://leetcode.cn/problems/reverse-pairs/description/
"""
from typing import List


class Solution:

    def merge_sort(self, nums: List[int], helper: List[int], left: int, right: int) -> int:
        if left == right:
            return 0
        mid = left + (right - left) // 2
        cnt1 = self.merge_sort(nums, helper, left, mid)  # 左边
        cnt2 = self.merge_sort(nums, helper, mid + 1, right)  # 右边
        cnt = 0  # 中间
        idx = mid + 1
        for i in range(left, mid + 1):
            while idx <= right and nums[i] > 2 * nums[idx]:
                idx += 1
            cnt += idx - mid - 1
        i, j, k = left, mid + 1, left
        while i <= mid or j <= right:
            if i > mid:
                helper[k] = nums[j]
                j += 1
            elif j > right:
                helper[k] = nums[i]
                i += 1
            else:
                if nums[i] <= nums[j]:
                    helper[k] = nums[i]
                    i += 1
                else:
                    helper[k] = nums[j]
                    j += 1
            k += 1
        for k in range(left, right + 1):
            nums[k] = helper[k]
        return cnt1 + cnt + cnt2

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        helper = [0] * n
        return self.merge_sort(nums, helper, 0, n - 1)
