# LC 206 Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# 迭代三指针：先存 nxt，再反转 cur.next，pre/cur 前移。O(n) / O(1)

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
