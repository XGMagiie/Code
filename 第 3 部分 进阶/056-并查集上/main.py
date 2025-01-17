class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.father = [-1] * (m * n)
        self.rank = [0] * (m * n)  # 树高
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                self.father[i * n + j] = i * n + j
                self.count += 1

    def find(self, i):
        if self.father[i] != i:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            if self.rank[fx] < self.rank[fy]:
                fx, fy = fy, fx
            self.father[fy] = fx
            if self.rank[fx] == self.rank[fy]:
                self.rank[fx] += 1
            self.count -= 1

    def getCount(self):
        return self.count
