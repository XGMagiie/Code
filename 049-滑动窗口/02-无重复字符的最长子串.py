"""
    3.无重复字符的最长子串
    https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # last = defaultdict(int)  记录上次出现的位置
        st = set()
        left = ans = 0
        for right, ch in enumerate(s):
            while ch in st:
                st.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            st.add(ch)
        return ans
