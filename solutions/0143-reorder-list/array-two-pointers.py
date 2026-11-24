# LC 143 Reorder List
# https://leetcode.com/problems/reorder-list/
# 节点存数组，左右下标交替接；奇数时中间节点只接一次，最后尾节点 .next = None。O(n) / O(n)

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
            if left > right:
                break
            cur.next = order[right]
            right-=1
            cur = cur.next
        cur.next = None
        return dummy_head.next
