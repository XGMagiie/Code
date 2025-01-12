"""
    210.课程表2  拓扑排序 邻接表 + 队列
    https://leetcode.cn/problems/course-schedule-ii/description/
"""
from collections import deque, defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # g = [[] for _ in range(numCourses)]
        g = defaultdict(list)
        degree = [0] * numCourses  # 入度
        for v, u in prerequisites:
            g[u].append(v)
            degree[v] += 1
        # 收集入度为 0 的节点
        q = deque(i for i in range(numCourses) if degree[i] == 0)
        ans = list()
        while q:
            u = q.popleft()
            ans.append(u)
            # 更新相邻节点的入度
            for v in g[u]:
                degree[v] -= 1
                # 入度为 0 的节点入队
                if degree[v] == 0:
                    q.append(v)
        return ans if len(ans) == numCourses else []
