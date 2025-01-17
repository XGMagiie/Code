"""
    3397.地毯   二维差分
    https://www.luogu.com.cn/problem/P3397
"""
n, m = map(int, input().split())

diff = [[0] * (n + 2) for _ in range(n + 2)]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    diff[x1][y1] += 1
    diff[x2 + 1][y1] -= 1
    diff[x1][y2 + 1] -= 1
    diff[x2 + 1][y2 + 1] += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        print(diff[i][j], end=' ')
    print()
