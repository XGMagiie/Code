"""
    85.最大矩形  必须以第 i 行为底 求最大面积(04-柱状图中的最大矩形)
    https://leetcode.cn/problems/maximal-rectangle/description/
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        h = [0] * n
        ans = 0
        for i in range(m):  # 以第 i 行做底
            for j in range(n):  # 更新 h 数组  h[i] 表示列 1 的个数
                h[j] = h[j] + 1 if matrix[i][j] == '1' else 0
            ans = max(ans, self.largestRectangleArea(h))
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = list()  # 单调栈
        left, right = [0] * n, [n] * n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                right[st.pop()] = i
            left[i] = st[-1] if st else -1
            st.append(i)
        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))
