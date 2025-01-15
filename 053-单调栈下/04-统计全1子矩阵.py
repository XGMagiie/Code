"""
    1504.统计全1子矩阵  以第 i 行为底 枚举高度  左右小于当前值
    https://leetcode.cn/problems/count-submatrices-with-all-ones/description/
"""
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                h[j] = h[j] + 1 if mat[i][j] == 1 else 0
            ans += self.cnt(h)
        return ans

    def cnt(self, h: List[int]) -> int:
        st = list()  # 用于求左边和右边小于当前值的下标
        left, ans = 0, 0
        # 遍历阶段
        for right, x in enumerate(h):
            while st and h[st[-1]] >= x:
                cur = st.pop()
                if h[cur] > h[right]:  # 二者相等不计算
                    left = st[-1] if st else -1
                    # 以被弹出的高度（必须大于左右两边的高度）统计答案
                    height = h[cur] - max(h[left] if st else 0, h[right])
                    # (left, right) 中高度为 max(h[left], h[right]) + 1 ~ h[cur] 的个数
                    # 个数为 left+1 .... right-1 == 1 + 2 + ... (right - left - 1)
                    ans += height * (right - left - 1) * (right - left) // 2
            st.append(right)
        # 清算阶段
        while st:
            cur = st.pop()
            left = st[-1] if st else -1
            # 右端点在最右边 高度为 0
            height = h[cur] - (h[left] if st else 0)
            ans += height * (len(h) - left - 1) * (len(h) - left) // 2
        return ans
