"""
    76.最小覆盖子串
    https://leetcode.cn/problems/minimum-window-substring/description/
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        cnt = Counter(t)
        debt = len(cnt)
        # start 起始位置  ans 最短长度
        left, start, ans = 0, 0, m + 1
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            if cnt[ch] == 0:  # 当前字符 ch 全部还完
                debt -= 1
            while debt == 0:  # 当前窗口已经覆盖了 t
                if right - left + 1 < ans:  # 更新答案
                    start, ans = left, right - left + 1
                if cnt[s[left]] == 0:  # 不会统计其他字符
                    debt += 1
                cnt[s[left]] += 1
                left += 1
        return s[start: start+ans] if ans != m + 1 else ""
