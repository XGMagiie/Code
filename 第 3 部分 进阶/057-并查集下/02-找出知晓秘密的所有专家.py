"""
    2092.找出知晓秘密的所有专家  打标签 + 取消合并
    https://leetcode.cn/problems/find-all-people-with-secret/description/
"""
from typing import List


class UnionFind:
    def __init__(self, n: int, first: int):
        self.__father = list(range(n))
        # 标记结合代表元素是否知道秘密
        self.__secret = [False] * n
        self.__father[first] = 0  # 0 分享给 first
        self.__secret[0] = True  # 0 知道秘密

    def find(self, a: int) -> int:
        if self.__father[a] != a:
            self.__father[a] = self.find(self.__father[a])
        return self.__father[a]

    def union(self, a: int, b: int) -> None:
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return
        self.__father[fa] = fb  # fa -> fb
        self.__secret[fb] |= self.__secret[fa]  # fb 代表元素

    def isSecret(self, a: int) -> bool:
        return self.__secret[self.find(a)]

    def rollback(self, a: int) -> None:
        # 拆分不知道秘密的集合
        if not self.isSecret(a):  # a 不知道秘密
            self.__father[a] = a


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        uf = UnionFind(n, firstPerson)
        """ 对于每一个时刻的会议分享秘密完后拆分不知道秘密的集合 """
        m, left = len(meetings), 0
        while left < m:
            right = left + 1
            while right < m and meetings[left][2] == meetings[right][2]:
                right += 1
            # [left...right) 处于同一时间
            for x, y, _ in meetings[left: right]:
                uf.union(x, y)
            # 拆分不知道秘密的集合
            for x, y, _ in meetings[left: right]:
                uf.rollback(x)
                uf.rollback(y)
            left = right

        return [i for i in range(n) if uf.isSecret(i)]
