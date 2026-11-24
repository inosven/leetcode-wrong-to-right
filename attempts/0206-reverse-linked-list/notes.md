# LC 206 Reverse Linked List

## 2026-11-23 · B · 5min

- 贴上来的版本正确（作为 LC 143 重排链表"反转后半段"的前置练习）。
- invariant：pre 是已反转部分的头，cur 是未反转部分的头；先存 nxt 再改 cur.next（先读后改）。
- 复杂度：O(n) / O(1)。迭代已最优；递归版 O(n) 栈空间，长链表有递归深度问题。
