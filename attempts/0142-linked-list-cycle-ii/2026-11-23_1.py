# LC 142 Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/
# 日期: 2026-11-23 | 章节: 链表 | 结果: B | 用时: 10min

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None

        p = head

        while True:
            p = p.next
            slow = slow.next
            if p == slow:
                return p
