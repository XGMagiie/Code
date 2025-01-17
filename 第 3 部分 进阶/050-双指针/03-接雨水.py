"""
    42.接雨水  升级(二维接雨水)  每一列上面能放多少格水
    https://leetcode.cn/problems/trapping-rain-water/description/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [height[0]] * n
        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i])
        rmax = [height[n - 1]] * n
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])
        ans = 0
        for i in range(1, n - 1):
            ans += max(min(lmax[i - 1], rmax[i + 1]) - height[i], 0)
        return ans

    def trap2(self, height: List[int]) -> int:  # 优化掉空间
        n = len(height)
        lmax, rmax = height[0], height[n - 1]
        ans, i, j = 0, 1, n - 2
        while i <= j:
            if lmax <= rmax:  # 需要移动左边
                if lmax > height[i]:  # 可以积水
                    ans += lmax - height[i]
                else:  # 不可以积水
                    lmax = height[i]
                i += 1
            else:  # 需要移动右边
                if rmax > height[j]:  # 可以积水
                    ans += rmax - height[j]
                else:  # 不可以积水
                    rmax = height[j]
                j -= 1
        return ans
