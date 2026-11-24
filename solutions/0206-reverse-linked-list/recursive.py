# LC 206 Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# 递归：reverse(pre, cur) 返回反转后的新头，每层都要 return 往上传。O(n) / O(n) 栈

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(pre,cur):
            if not cur:
                return pre
            nxt = cur.next
            cur.next = pre
            return reverse(cur,nxt)
        return reverse(None,head)
