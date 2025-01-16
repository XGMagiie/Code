"""
    牛客.线段重合
    https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37
"""
from heapq import heappush, heappop

n = int(input())
data = [[0, 0] for _ in range(n)]
for i in range(n):
    data[i][0], data[i][1] = map(int, input().split())
data.sort(key=lambda x: x[0])

h = []  # 小根堆
ans = 0
for s, e in data:
    while h and h[0] <= s:
        heappop(h)  # 此时边不会影响后续
    heappush(h, e)
    ans = max(ans, len(h))
print(ans)
