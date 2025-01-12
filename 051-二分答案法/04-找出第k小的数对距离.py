"""
    719.找出第k小的距离对  滑动窗口求满足数对的个数
    https://leetcode.cn/problems/find-k-th-smallest-pair-distance/description/
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def check(x: int) -> bool:
            # 滑动窗口求数对个数
            left, right, cnt = 0, 0, 0
            while right < n:
                while nums[right] - nums[left] > x:
                    left += 1
                # nums[left...right-1] 与 nums[right] 都满足
                cnt += right - left
                right += 1
            return cnt >= k

        nums.sort()
        n = len(nums)
        low, high = 0, nums[n - 1] - nums[0]
        # 找第一个大于等于 bisect_left
        while low < high:
            mid = low + (high - low) // 2
            if check(mid):  # 当前值可能是答案
                high = mid
            else:  # 当前值不是答案
                low = mid + 1
        return low
