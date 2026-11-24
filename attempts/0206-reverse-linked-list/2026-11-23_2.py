# LC 206 Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# 日期: 2026-11-23 | 章节: 链表 | 结果: B | 用时: 5min（递归版，与迭代版同一次）

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(pre,cur):
            if not cur:
                return pre
            nxt = cur.next
            cur.next = pre
            reverse(cur,nxt)
        return reverse(None,head)
