"""
    912.排序数组  快速排序
    https://leetcode.cn/problems/sort-an-array/description/
"""
from random import randint
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(arr: List[int], low: int, high: int) -> None:
            if low >= high:  # 递归结束
                return
            pivot_idx = randint(low, high)  # 随机选择 pivot
            arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]  # pivot 放置到最右边
            pivot = arr[high]  # 选取最右边为 pivot

            left = low - 1  # 双指针
            for right in range(low, high):
                if nums[right] <= pivot:
                    left += 1
                    nums[left], nums[right] = nums[right], nums[left]
            nums[left + 1], nums[high] = nums[high], nums[left + 1]

            mid = left + 1
            quick_sort(arr, low, mid - 1)  # 递归对 mid 两侧元素进行排序
            quick_sort(arr, mid + 1, high)

        quick_sort(nums, 0, len(nums) - 1)  # 调用快排函数对 nums 进行排序
        return nums
