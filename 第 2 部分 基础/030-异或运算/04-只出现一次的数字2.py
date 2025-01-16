"""
    137.只出现一次的数字II  一个出现m次 其他出现n次
    https://leetcode.cn/problems/single-number-ii/description/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = 3
        ans = 0
        for i in range(32):
            cnt = 0
            for x in nums:
                cnt += (x >> i) & 1
            if cnt % m:
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans
