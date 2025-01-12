"""
    1234.替换子串得到平衡字符串  03-最小覆盖子串的变形  覆盖多余字符
    https://leetcode.cn/problems/replace-the-substring-for-balanced-string/description/
"""
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        cnt = Counter(s)
        debt = 4  # 欠的字符个数
        for ch in "QWER":
            if cnt[ch] <= n // 4:  # 不欠
                cnt[ch] = 0
                debt -= 1
            else:
                cnt[ch] -= n // 4
        if debt == 0:
            return 0
        # 覆盖 cnt 的最小子串
        left, ans = 0, n + 1
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            if cnt[ch] == 0:  # 当前字符 ch 全部还完
                debt -= 1
            while debt == 0:  # 当前窗口已经覆盖了 cnt
                if right - left + 1 < ans:  # 更新答案
                    ans = right - left + 1
                if cnt[s[left]] == 0:  # 不会统计其他字符
                    debt += 1
                cnt[s[left]] += 1
                left += 1
        return ans
