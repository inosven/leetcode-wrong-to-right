# LC 206 Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# 日期: 2026-11-23 | 章节: 链表 | 结果: B | 用时: 5min

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur =nxt
        return pre
