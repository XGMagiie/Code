"""
    牛客.合并K个已排序的链表
    https://www.nowcoder.com/practice/65cfde9e5b9b4cf2b6bafa5f3ef33fa6
"""
from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()  # 小顶堆
        # 遍历所有链表第一个元素
        for i in range(len(lists)):
            # 不为空则加入小顶堆
            if lists[i]:
                pq.put((lists[i].val, i))
                lists[i] = lists[i].next
        res = ListNode(-1)  # 哨兵节点
        head = res
        while not pq.empty():  # 直到小顶堆为空
            val, idx = pq.get()  # 取出最小的元素
            head.next = ListNode(val)
            head = head.next
            if lists[idx]:
                # 每次取出链表的后一个元素加入小顶堆
                pq.put((lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return res.next
