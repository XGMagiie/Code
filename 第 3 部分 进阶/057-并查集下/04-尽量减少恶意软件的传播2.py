"""
    928.尽量减少恶意软件的传播II  普通点  病毒点  统计个数
    https://leetcode.cn/problems/minimize-malware-spread-ii/description/
"""
from typing import List


class UnionFind:
    def __init__(self, n: int, initial: List[int]):
        self.__father = list(range(n))
        self.__size = [1] * n  # 集合的大小

        self.__infect = [-1] * n  # 与集合关联的病毒点
        self.__virus = [False] * n  # 标记是否为病毒
        for idx in initial:
            self.__virus[idx] = True

        self.__cnt = [0] * n  # 删除病毒拯救点的个数

    def find(self, a: int) -> int:
        if self.__father[a] != a:
            self.__father[a] = self.find(self.__father[a])
        return self.__father[a]

    def union(self, a: int, b: int) -> None:
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return
        self.__father[fb] = fa
        self.__size[fa] += self.__size[fb]

    def summary(self, n: int) -> None:
        for i in range(n):
            # 统计每个病毒的关联集合大小
            if i == self.find(i) and self.__infect[i] >= 0:
                self.__cnt[self.__infect[i]] += self.__size[i]

    def isVirus(self, a: int) -> bool:
        return self.__virus[a]

    def setInfect(self, a: int, virus: int) -> None:
        fa = self.find(a)
        if self.__infect[fa] == -1:
            self.__infect[fa] = virus  # 第一次出现病毒点
        elif self.__infect[fa] != -2 and self.__infect[fa] != virus:
            self.__infect[fa] = -2  # 多个病毒点

    def getCnt(self, a: int) -> int:
        return self.__cnt[a]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n, initial)
        # 1 合并普通点
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1 and not uf.isVirus(i) and not uf.isVirus(j):
                    uf.union(i, j)
        # 2 给病毒相连集合设置源头
        for virus in initial:
            for i in range(n):
                if graph[virus][i] == 1 and virus != i and not uf.isVirus(i):
                    uf.setInfect(i, virus)
        # 3 统计拯救数据
        uf.summary(n)

        mx, idx = -1, -1  # 返回最大值下标
        for i in initial:
            if uf.getCnt(i) > mx:
                idx = i
                mx = uf.getCnt(i)
            elif uf.getCnt(i) == mx:
                idx = min(idx, i)
        return idx
