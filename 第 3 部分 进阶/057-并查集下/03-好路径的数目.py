"""
    2421.好路径的数目  最大值下标和最大值个数 + 排序  计算每条边的共享次数
    https://leetcode.cn/problems/number-of-good-paths/description/
"""
from typing import List


class UnionFind:
    def __init__(self, vals: List[int]):
        self.__vals = vals
        self.__father = list(range(len(vals)))  # 代表元素是最大值
        self.__cnt = [1] * len(vals)  # 最大值的个数

    def find(self, a: int) -> int:
        if self.__father[a] != a:
            self.__father[a] = self.find(self.__father[a])
        return self.__father[a]

    def union(self, a: int, b: int) -> int:  # 返回路径个数
        fa, fb = self.find(a), self.find(b)
        # 谁大谁做代表结点
        path = 0  # 好路径条数
        if self.__vals[fa] > self.__vals[fb]:
            self.__father[fb] = fa
        elif self.__vals[fa] < self.__vals[fb]:
            self.__father[fa] = fb
        else:  # 此时会产生好路径
            path = self.__cnt[fa] * self.__cnt[fb]
            self.__father[fb] = fa
            self.__cnt[fa] += self.__cnt[fb]
        return path


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        uf = UnionFind(vals)
        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))
        ans = len(vals)
        for u, v in edges:
            ans += uf.union(u, v)
        return ans
