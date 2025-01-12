"""
    475.供暖器  变小不更新  超过阈值更新
    https://leetcode.cn/problems/heaters/description/
"""
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        i, j = 0, 0  # 房间下标 供暖器下标
        while i < len(houses):
            # 寻找最优的供暖器
            while j < len(heaters) - 1 and abs(heaters[j] - houses[i]) >= abs(heaters[j + 1] - houses[i]):
                # 最优：右边的供暖器比当前供暖器差
                j += 1
            ans = max(ans, abs(heaters[j] - houses[i]))
            i += 1
        return ans
