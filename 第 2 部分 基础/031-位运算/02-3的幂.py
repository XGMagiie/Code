"""
    326.3的幂   1162261467 为最大的 3 的幂
    https://leetcode.cn/problems/power-of-three/description/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
