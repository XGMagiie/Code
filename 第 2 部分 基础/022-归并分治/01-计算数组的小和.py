"""
    牛客.计算数组的小和  归并分治
    https://www.nowcoder.com/questionTerminal/edfe05a1d45c4ea89101d936cac32469
"""
from typing import List


def mergeSort(nums: List[int], helper: List[int], left: int, right: int) -> int:
    if left >= right:
        return 0
    mid = left + (right - left) // 2
    cnt1 = mergeSort(nums, helper, left, mid)  # 左边
    cnt2 = mergeSort(nums, helper, mid + 1, right)  # 右边
    cnt = 0  # 中间
    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:  # 小和
            # nums[i] 是 j ... right 的小和
            cnt += nums[i] * (right - j + 1)
            helper[k] = nums[i]
            i += 1
        else:
            helper[k] = nums[j]
            j += 1
        k += 1
    while i <= mid:
        helper[k] = nums[i]
        i, k = i + 1, k + 1
    while j <= right:
        helper[k] = nums[j]
        j, k = j + 1, k + 1
    for k in range(left, right + 1):
        nums[k] = helper[k]
    return cnt1 + cnt + cnt2


N = int(input())
nums = list(map(int, input().split()))
helper = [0] * N
print(mergeSort(nums, helper, 0, N - 1))
