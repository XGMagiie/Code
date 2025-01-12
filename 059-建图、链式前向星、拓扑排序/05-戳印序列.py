"""
    936.戳印序列  拓扑排序  逆向思维
    https://leetcode.cn/problems/stamping-the-sequence/description/
    aabcbc  abc
    0 aab  1(0)0(1)0(2)[2] -> 1(0)1(1)1(2)[0] -> 2 (0 1 2 3)
    1 abc  1(1)1(2)1(3)[0] 1 (1 2 3)
    2 bcc  0(2)0(3)0(4)[3] -> 1(2)1(3)0(4)[1] -> 1(2)1(3)0(4)[1] -> 1(2)1(3)1(4)[0] -> 4 (0 1 2 3 4 5)
    3 cbc  0(3)1(4)1(5)[1] -> 1(3)1(4)1(5)[0] -> 1(3)1(4)1(5)[0] -> 3 (0 1 2 3 4 5)
    1 -> 0 -> 3 -> 2 答案为逆序
"""
from collections import deque
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        g = [[] for _ in range(n)]  # target 每个位置
        degree = [m] * (n - m + 1)  # 假设起始所有位置都是错误的
        # 收集度数为 0 的结点 并建图
        q = deque()
        for i in range(n - m + 1):
            for j in range(m):
                if stamp[j] == target[i + j]:  # 匹配上
                    degree[i] -= 1  # 当前位置入度减 1
                    if degree[i] == 0:
                        q.append(i)
                else:
                    # target[i + j] 位置发生错误 因为 i 作为 stamp 开头
                    g[i + j].append(i)
        vis = set()  # 每个点只更新一次
        ans = list()
        while q:
            u = q.popleft()
            ans.append(u)
            # 跟新 u  u + 1 ... u + m - 1 的位置
            for i in range(m):
                if u + i in vis:
                    continue
                vis.add(u + i)
                for v in g[u + i]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        q.append(v)
        if len(ans) != n - m + 1:
            return []  # 没有全部匹配上
        ans.reverse()  # 反转输出
        return ans
