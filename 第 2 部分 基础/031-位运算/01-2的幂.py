"""
    231.2的幂
    https://leetcode.cn/problems/power-of-two/description/
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and n == n & (-n)
