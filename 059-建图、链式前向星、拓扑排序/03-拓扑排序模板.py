"""
    U107394.拓扑排序模板  拓扑排序  链式前向星 + 堆
    https://www.luogu.com.cn/problem/U107394
"""
from heapq import heappush, heappop


class Graph:
    def __init__(self, n, m):
        # n 点数  m 边数
        self.n = n  # 下标从 1 开始
        self.m = m  # 无向图需要乘以 2

        self.head = [0] * (n + 1)  # 头边号 每个点关联的边串成一条链
        self.nxt = [0] * (m + 1)  # 下一条边号 类似链表
        self.to = [0] * (m + 1)  # 每条边去往的点号

        self.cnt = 1  # 具体边的个数

    def add(self, u: int, v: int) -> None:
        self.nxt[self.cnt] = self.head[u]  # 这条边的作 u 的头边号
        self.head[u] = self.cnt  # 更新头边号
        self.to[self.cnt] = v  # 这条边去 v
        self.head[u] = self.cnt  # 更新头边号
        self.cnt += 1


n, m = map(int, input().split())
g = Graph(n, m)
degree = [0] * (n + 1)  # 入度
for _ in range(m):
    u, v = map(int, input().split())
    g.add(u, v)
    degree[v] += 1

# 收集入度为 0 的节点
h = list()
for i in range(1, n + 1):
    if degree[i] == 0:
        heappush(h, i)
ans = list()
while h:
    u = heappop(h)
    ans.append(u)
    # 更新相邻节点的入度
    e = g.head[u]
    while e > 0:
        degree[g.to[e]] -= 1  # 邻接点的度数减 1
        # 入度为 0 的节点入队
        if degree[g.to[e]] == 0:
            heappush(h, g.to[e])
        e = g.nxt[e]
print(*ans)
