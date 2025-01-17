"""
    907.子数组的最小值之和  计算以每个值为最小值的子数组个数
    https://leetcode.cn/problems/sum-of-subarray-minimums/description/
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        # 1 求左边 严格大于当前值
        st = list()  # 找左边和右边第一个小于当前值的下标
        left = [0] * n
        for i in range(n):
            while st and arr[i] <= arr[st[-1]]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        # 2 求右边  大于等于即可
        st.clear()
        right = [0] * n
        for i in range(n - 1, -1, -1):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        # 3 计算累计共享 min(left[i]..i..right[i]) = i
        ans = 0
        for i in range(n):
            ans += arr[i] * (i - left[i]) * (right[i] - i)
            ans %= MOD
        return ans

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        # 1 求左边 严格大于当前值 右边大于等于当前值
        st = list()  # 找左边和右边第一个小于当前值的下标
        left, right = [0] * n, [n] * n
        for i in range(n):
            while st and arr[i] <= arr[st[-1]]:
                right[st.pop()] = i  # i 是栈顶的右端点
            left[i] = st[-1] if st else -1
            st.append(i)
        # 2 计算累计共享 min(left[i]..i..right[i]) = i
        ans = 0
        for i in range(n):
            ans += arr[i] * (i - left[i]) * (right[i] - i)
            ans %= MOD
        return ans
