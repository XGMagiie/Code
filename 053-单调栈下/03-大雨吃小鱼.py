"""
    牛客.大雨吃小鱼   (体重 轮数) 按体重从大到小  相等不弹出
    https://www.nowcoder.com/practice/77199defc4b74b24b8ebf6244e1793de
"""
n = int(input())
a = list(map(int, input().split()))
st = list()  # (体重 轮数) 按体重从大到小
ans = 0
for i in range(n - 1, -1, -1):
    idx = 0
    while st and st[-1][0] < a[i]:  # 相等不弹出
        idx = max(idx + 1, st.pop()[1])
    st.append((a[i], idx))
    ans = max(ans, idx)
print(ans)
