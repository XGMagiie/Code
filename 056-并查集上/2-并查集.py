"""
    P3367.【模板】并查集  递归 find
    https://www.luogu.com.cn/problem/P3367
"""
n, m = map(int, input().split())
father = list(range(n + 1))


def find(a: int) -> int:
    if a != father[a]:
        # 将 a 的父亲改为 father[a] 的父亲
        father[a] = find(father[a])
    return father[a]


def isSameSet(a: int, b: int) -> bool:
    return find(a) == find(b)


def union(a: int, b: int) -> None:
    father[find(a)] = find(b)


for _ in range(m):
    z, x, y = map(int, input().split())
    if z == 1:
        union(x, y)
    else:
        print("Y" if isSameSet(x, y) else "N")
