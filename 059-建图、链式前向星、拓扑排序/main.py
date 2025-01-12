from typing import List


class Graph:
    def __init__(self, n: int, m: int):
        # n 点数  m 边数
        self.n = n  # 下标从 1 开始
        self.m = m << 1  # 无向图需要乘以 2

        self.head = [0] * (n + 1)  # 头边号 每个点关联的边串成一条链
        self.nxt = [0] * (m + 1)  # 下一条边号 类似链表
        self.to = [0] * (m + 1)  # 每条边去往的点号
        self.weight = [0] * (m + 1)  # 边权

        self.cnt = 1  # 具体边的个数

    def add(self, u: int, v: int, w: int) -> None:
        self.nxt[self.cnt] = self.head[u]  # 这条边的作 u 的头边号
        self.head[u] = self.cnt  # 更新头边号
        self.to[self.cnt] = v  # 这条边去 v
        self.weight[self.cnt] = w  # 这条边的权值
        self.head[u] = self.cnt  # 更新头边号
        self.cnt += 1

    def directed(self, edges: List[List[int]]) -> None:  # 有向图
        for u, v, w in edges:
            self.add(u, v, w)

    def undirected(self, edges: List[List[int]]) -> None:  # 无向图
        for u, v, w in edges:
            self.add(u, v, w)
            self.add(v, u, w)

    def traversal(self) -> None:
        for i in range(1, self.n + 1):
            e = self.head[i]
            while e > 0:  # 边结尾均指向 0
                print(f'{i} -> {self.to[e]} weight: {self.weight[e]}')
                e = self.nxt[e]
