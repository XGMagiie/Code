"""
    395.至少有K个重复字符的最长子串  每个字符都要 >= k == max(1个字符满足  2个字符满足 .. 26个字符满足)
    https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""
from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for i in range(1, 27):  # 窗口必须有 i 个字符 且个数都要 >= k
            cnt = defaultdict(int)
            left = 0  # 左边界
            collect = 0  # 总共的种类个数
            satisfy = 0  # 满足条件的种类个数
            for right, ch in enumerate(s):
                if cnt[ch] == 0:
                    collect += 1  # 总共种类数增加
                cnt[ch] += 1
                if cnt[ch] == k:
                    satisfy += 1  # 满足的种类数增加
                # 移动左端点
                while collect > i:  # 种类数过多
                    if cnt[s[left]] == k:
                        satisfy -= 1  # 满足的种类数减少
                    cnt[s[left]] -= 1
                    if cnt[s[left]] == 0:
                        collect -= 1  # 总共种类数减少
                    left += 1
                # 记录答案
                if satisfy == i:
                    ans = max(ans, right - left + 1)
        return ans
