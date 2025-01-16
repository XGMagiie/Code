"""
    201.数字范围按位与
    https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right -= right & (-right)  # 抹去最右边的 1
        return right
