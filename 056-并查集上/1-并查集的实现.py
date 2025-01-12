"""
    并查集的实现  非递归 find
    https://www.nowcoder.com/practice/e7ed657974934a30b2010046536a5372
"""
n, m = map(int, input().split())
father = list(range(n + 1))
size = [1] * (n + 1)


def find(a: int) -> int:
    """  1 扁平化 """
    stack = list()  # 收集沿途结点
    while a != father[a]:
        stack.append(a)
        a = father[a]
    while stack:  # 将结点全部指向头
        father[stack.pop()] = a
    return a


def isSameSet(a: int, b: int) -> bool:
    return find(a) == find(b)


def union(a: int, b: int) -> None:
    fa, fb = find(a), find(b)
    if fa == fb:  # 属于同一集合
        return
    """ 2 小挂大 """
    if size[fa] >= size[fb]:
        size[fa] += size[fb]
        father[fb] = fa
    else:
        size[fb] += size[fa]
        father[fa] = fb


for _ in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        print("Yes" if isSameSet(x, y) else "No")
    else:
        union(x, y)
