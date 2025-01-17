"""
    牛客.机器人跳跃问题  bisect_left
    https://www.nowcoder.com/practice/7037a3d57bbd4336856b8e16a9cafd71
"""
n = int(input())
h = list(map(int, input().split()))


def check(x: int) -> bool:
    for i in range(n):
        if h[i] >= x:
            x -= h[i] - x
        else:
            x += x - h[i]
        if x < 0:
            return False
    return True


low, high = 0, max(h)
# 找第一个大于等于 bisect_left
while low < high:
    mid = low + (high - low) // 2
    if check(mid):  # 当前可能是答案
        high = mid
    else:  # 当前不是答案
        low = mid + 1
print(low)
