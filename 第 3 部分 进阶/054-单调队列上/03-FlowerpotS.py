"""
    洛谷 2698.[USACO07JAN]FlowerpotS S  两个单调队列维护最大最小值
    https://www.luogu.com.cn/problem/P2698
"""
from collections import deque
from math import inf

N, D = map(int, input().split())
nums = [[0, 0] for _ in range(N)]
for i in range(N):
    nums[i][0], nums[i][1] = map(int, input().split())
nums.sort(key=lambda x: x[0])  # 第一项是位置  第二项是高度

Max, Min = deque(), deque()   # 维持区间内最大最小值
left, ans = 0, inf
for right in range(N):
    while Max and Max[-1] < nums[right][1]:
        Max.pop()
    while Min and Min[-1] > nums[right][1]:
        Min.pop()
    Max.append(nums[right][1])
    Min.append(nums[right][1])
    while Max and Min and Max[0] - Min[0] >= D:
        # 记录答案
        ans = min(ans, nums[right][0] - nums[left][0])
        if Max[0] == nums[left][1]:
            Max.popleft()
        if Min[0] == nums[left][1]:
            Min.popleft()
        left += 1
print(ans if ans != inf else -1)
