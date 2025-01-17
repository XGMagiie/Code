"""
    839.相似字符串组   集合个数 + 字符相似
    https://leetcode.cn/problems/similar-string-groups/description/
"""
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        father = list(range(n))
        sets = n

        def find(a: int) -> int:
            if a != father[a]:
                father[a] = find(father[a])
            return father[a]

        def union(a: int, b: int) -> None:
            fa, fb = find(a), find(b)
            if fa == fb:
                return
            father[fa] = fb
            nonlocal sets
            sets -= 1

        for i in range(n):
            for j in range(i + 1, n):
                if find(i) == find(j):  # 是相同字符
                    continue
                m, diff = len(strs[0]), 0
                for ci, cj in zip(strs[i], strs[j]):
                    if ci != cj:
                        diff += 1
                    if diff > 3:  # 提前终止
                        break
                if diff == 0 or diff == 2:  # 只会出现偶数的情形
                    union(i, j)  # strs[i] 与 strs[j] 相似
        return sets
