"""
    947.移除最多的同行或同列石头  用哈希表记录行列下标
    https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/description/
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.__father = list(range(n))
        self.__sets = n

    def find(self, a: int) -> int:
        if self.__father[a] != a:
            self.__father[a] = self.find(self.__father[a])
        return self.__father[a]

    def union(self, a: int, b: int) -> None:
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return
        self.__father[fa] = fb
        self.__sets -= 1

    def getCount(self) -> int:
        return self.__sets


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))

        row, col = dict(), dict()  # {行号/列号 : 石头下标}
        for i, (r, c) in enumerate(stones):
            if r in row:  # 需要合并
                uf.union(i, row[r])
            else:  # 放入
                row[r] = i
            if c in col:  # 需要合并
                uf.union(i, col[c])
            else:  # 放入
                col[c] = i
        return len(stones) - uf.getCount()
