"""
    316.去除重复字母  栈中字符保持从小到大 特殊除外
    https://leetcode.cn/problems/remove-duplicate-letters/description/
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)  # 字符个数
        st = set()  # 记录字母是否进栈
        stack = list()  # 单调栈 保持从小到大 特殊除外
        for ch in s:
            if ch not in st:  # 保证当前字符不在栈中
                while stack and stack[-1] > ch and cnt[stack[-1]] > 0:  # 可以弹出栈顶
                    st.remove(stack.pop())
                # 加入栈中
                stack.append(ch)
                st.add(ch)
            cnt[ch] -= 1
        return "".join(stack)
