"""
    2071.你可以安排的最多任务数目  二分需要满足条件的最大值 + 贪心 + 双端队列
    https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/description/
"""
from collections import deque
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        workers.sort(reverse=True)

        def f(x: int) -> bool:  # 是否能在给定的条件下完成 x 个任务
            # 任务选小的 tasks[:x]  工人选大的 workers[:x]  最后判断吃的药物个数是否超过给定值
            q = deque()  # 存放任务
            cnt, j = 0, 0  # j 是任务的编号
            for i in range(x - 1, -1, -1):  # 对于每个工人找合适的任务
                # 1 将工人不吃药能解锁的任务加入队列
                while j < x and tasks[j] <= workers[i]:
                    q.append(tasks[j])
                    j += 1
                # 2 如果工人有任务做则做 否则吃药
                if q and q[0] <= workers[i]:
                    q.popleft()
                else:  # 需要吃药
                    while j < x and tasks[j] <= workers[i] + strength:
                        q.append(tasks[j])  # 将吃完药能解锁的任务加入队列
                        j += 1
                    if q:  # 吃了药可以做任务
                        cnt += 1
                        q.pop()  # 弹出此时最大能做的任务
                    else:  # 吃了药不能做任务
                        return False
            return cnt <= pills

        low, high = 0, min(n, m)
        # 寻找第一个大于当前值的前一位 bisect_right - 1
        while low < high:
            mid = low + (high - low + 1) // 2  # 二分任务数
            if f(mid):  # 满足
                low = mid
            else:
                high = mid - 1  # 当前不可能是答案
        return low
