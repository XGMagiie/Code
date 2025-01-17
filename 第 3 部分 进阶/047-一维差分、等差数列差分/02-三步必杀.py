"""
    洛谷4231.三步必杀  等差数列差分
    https://www.luogu.com.cn/problem/P4231
    1 a[L] += s  a[L + 1] += d - s
    2 a[R + 1] -= d + e  a[R + 2] += e
    3 两遍前缀和

    最终结果：[0, 0, s, s + d, s + 2d, s + 3d, s + 4d(e),       0, 0]
    差分一次：[0, 0, s,     d,      d,      d,         d,     - e, 0]
    差分两次：[0, 0, s, d - s,      0,      0,         0, - e - d, e]
"""
n, m = map(int, input().split())
a = [0] * (n + 3)
for _ in range(m):
    l, r, s, e = map(int, input().split())
    d = (e - s) // (r - l)

    a[l] += s
    a[l + 1] += d - s
    a[r + 1] -= d + e
    a[r + 2] += e

for i in range(1, n + 3):
    a[i] += a[i - 1]

xor, mx = 0, 0
for i in range(1, n + 1):
    a[i] += a[i - 1]

    xor ^= a[i]
    mx = max(a[i], mx)

print(xor, mx)
