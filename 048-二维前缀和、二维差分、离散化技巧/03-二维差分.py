"""
    牛客.【模板】二维差分  二维差分
    https://www.nowcoder.com/practice/99eb8040d116414ea3296467ce81cbbc
    d[a][b] + k  d[c + 1][b] - k  d[a][d + 1] - k  d[c + 1][d + 1] + k
"""
n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

diff = [[0] * (m + 2) for _ in range(n + 2)]
for _ in range(q):
    x1, y1, x2, y2, k = map(int, input().split())

    diff[x1][y1] += k
    diff[x2 + 1][y1] -= k
    diff[x1][y2 + 1] -= k
    diff[x2 + 1][y2 + 1] += k

for i in range(1, n + 1):
    for j in range(1, m + 1):
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        print(a[i - 1][j - 1] + diff[i][j], end=' ')
    print()
