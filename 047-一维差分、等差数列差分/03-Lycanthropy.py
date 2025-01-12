"""
    洛谷5026.Lycanthropy  四次等差数列差分
    https://www.luogu.com.cn/problem/P5026
"""


def update(l: int, r: int, s: int, e: int, d: int) -> None:
    a[l + mx] += s
    a[l + 1 + mx] += d - s
    a[r + 1 + mx] -= d + e
    a[r + 2 + mx] += e


mx = 3_000_1  # 将数据下标规范到非负数
n, m = map(int, input().split())
a = [0] * (mx + m + 1 + mx)
for _ in range(n):
    v, x = map(int, input().split())

    update(x - 3 * v + 1, x - 2 * v, 1, v, 1)
    update(x - 2 * v + 1, x, v - 1, -v, -1)
    update(x + 1, x + 2 * v, -v + 1, v, 1)
    update(x + 2 * v + 1, x + 3 * v - 1, v - 1, 1, -1)

for i in range(1, m + 1 + mx):
    a[i] += a[i - 1]
for i in range(1, m + 1 + mx):
    a[i] += a[i - 1]
print(*a[mx + 1:mx + m + 1])
