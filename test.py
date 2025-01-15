from math import inf
from collections import deque

N, D = map(int, input().split())
nums = [[0, 0] for _ in range(N)]
for i in range(N):
    nums[i][0], nums[i][1] = map(int, input().split())
nums.sort(key=lambda x: x[0])

Max, Min = deque(), deque()  # 记录区间的最大最小值
left, ans = 0, inf
for right in range(N):
    while Max and Max[-1] < nums[right][1]:
        Max.pop()
    while Min and Min[-1] > nums[right][1]:
        Min.pop()
    Max.append(nums[right][1])
    Min.append(nums[right][1])
    while Max and Min and Max[0] - Min[0] >= D:
        ans = max(ans, nums[right][0] - nums[left][0])
        if Max[0] == nums[left]:
            Max.popleft()
        if Min[0] == nums[left]:
            Min.popleft()
        left += 1

print(ans if ans != inf else -1)
