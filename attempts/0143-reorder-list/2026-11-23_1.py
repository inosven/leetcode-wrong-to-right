# LC 143 Reorder List
# https://leetcode.com/problems/reorder-list/
# 日期: 2026-11-23 | 章节: 链表 | 结果: C | 用时: 25min（第 1 版）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        order = []
        while fast:
            order.append(fast)
            fast=fast.next
        
        n = len(order)
        left =0
        right = n-1

        dummy_head = ListNode(next=head)
        cur = dummy_head
        while left <= right:
            cur.next = order[left]
            left+=1
            cur = cur.next
            cur.next = order[right]
            right-=1
            cur = cur.next
        return dummy_head.next
