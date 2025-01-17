"""
    765.情侣牵手  情侣对数 - 集合个数
    https://leetcode.cn/problems/couples-holding-hands/description/
"""
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        father = list(range(n // 2 + 1))
        sets = n // 2  # 集合个数

        def find(a: int) -> int:
            if a != father[a]:
                # 将 a 的父亲改为 father[a] 的父亲
                father[a] = find(father[a])
            return father[a]

        def union(a: int, b: int) -> None:
            fa, fb = find(a), find(b)
            if fa == fb:  # 属于同一集合
                return
            father[fa] = fb
            nonlocal sets
            sets -= 1  # 集合个数减少

        for i in range(0, n, 2):
            union(row[i] // 2, row[i + 1] // 2)
        return n // 2 - sets
