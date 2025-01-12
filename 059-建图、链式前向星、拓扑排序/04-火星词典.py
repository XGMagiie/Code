"""
    269.火星词典 => LCR114.火星字典  拓扑排序  字符之间建边
    https://leetcode.cn/problems/Jf1JuT/description/
"""
from collections import defaultdict, deque
from itertools import pairwise
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # g = [[] for _ in range(26)]
        g = defaultdict(list)
        degree = {c: 0 for c in words[0]}  # 入度
        for s, t in pairwise(words):
            for c in t:  # 设置 t 均无前向边
                degree.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:  # 添加 u -> v 的边
                    g[u].append(v)
                    degree[v] += 1
                    break
            else:
                if len(s) > len(t):
                    return ""
        # 拓扑排序
        q = deque(i for i, x in degree.items() if x == 0)
        ans = ""
        while q:
            u = q.popleft()
            ans += u
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    q.append(v)
        return ans if len(ans) == len(degree) else ""
