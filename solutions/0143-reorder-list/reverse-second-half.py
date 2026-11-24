# LC 143 Reorder List
# https://leetcode.com/problems/reorder-list/
# 快慢指针找中点 → 先断开再反转后半段 → 交替合并（每轮改两根指针）。O(n) / O(1)

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
        def reverse(head):
            pre = None
            cur = head
            while cur:
                nxt= cur.next
                cur.next = pre
                pre = cur
                cur=nxt
            return pre
        
        def getmid(head):
            fast=slow=head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def merge(head1, head2):
            while head1 and head2:
                nxt1 = head1.next
                nxt2 = head2.next
                head1.next = head2
                head2.next = nxt1
                head1 = nxt1
                head2 = nxt2

        mid = getmid(head)
        second = mid.next
        mid.next = None
        secondhalf = reverse(second)
        merge(head,secondhalf)
