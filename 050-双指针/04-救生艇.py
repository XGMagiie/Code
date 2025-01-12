"""
    881.救生艇  升级(两个人的体重和必须为偶数)  贪心
    https://leetcode.cn/problems/boats-to-save-people/description/
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, left, right = 0, 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            ans += 1
        return ans
