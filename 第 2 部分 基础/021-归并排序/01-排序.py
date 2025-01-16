"""
    牛客.排序  归并排序
    https://www.nowcoder.com/practice/2baf799ea0594abd974d37139de27896
"""
from typing import List


class Solution:
    def merge_sort(self, nums: List[int], l: int, r: int) -> None:
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def MySort(self, arr: List[int]) -> List[int]:
        self.merge_sort(arr, 0, len(arr) - 1)
        return arr
