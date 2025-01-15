"""
    84.柱状图中最大的矩形  计算以每个数组为高度往左和右的最远距离
    https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = list()  # 单调栈
        left = [0] * n  # 记录左边第一个小于当前值的下标
        for i in range(n):  # 从左往右遍历
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        right = [0] * n  # 记录右边第一个小于当前值的下标
        for i in range(n - 1, -1, -1):  # 从右往左遍历
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))

    def largestRectangleArea2(self, heights: List[int]) -> int:
        n = len(heights)
        st = list()  # 单调栈
        left, right = [0] * n, [n] * n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                right[st.pop()] = i
            left[i] = st[-1] if st else -1
            st.append(i)
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))
