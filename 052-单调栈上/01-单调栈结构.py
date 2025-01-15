"""
    牛客.单调栈结构(进阶)  找左右两边小于当前值的下标
    https://www.nowcoder.com/practice/2a2c00e7a88a498693568cef63a4b7bb
"""
n = int(input())
arr = list(map(int, input().split()))
ans = [[0, 0] for _ in range(n)]
st = list()  # 单调栈 存储的是下标
# 1 遍历  找小于  从小到大
for i in range(n):
    while st and arr[st[-1]] >= arr[i]:
        idx = st.pop()
        ans[idx][0] = st[-1] if st else -1  # 左边小于当前值的下标
        ans[idx][1] = i   # 右边小于当前值的下标 i
    st.append(i)
# 2 清算  将栈内多余元素弹出
while st:
    idx = st.pop()
    ans[idx][0] = st[-1] if st else -1  # 左边小于当前值的下标
    ans[idx][1] = -1   # 右边小于当前值的下标不存在
# 3 修正  左边没问题  右侧如果相等则会出现问题
for i in range(n - 2, -1, -1):  # 倒叙遍历
    if ans[i][1] != -1 and arr[i] == arr[ans[i][1]]:
        ans[i][1] = ans[ans[i][1]][1]  # 修正相等的右侧
for l, r in ans:
    print(l, r)
