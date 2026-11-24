# LC 206 Reverse Linked List

## 2026-11-23 · B · 5min

- 贴上来的版本正确（作为 LC 143 重排链表"反转后半段"的前置练习）。
- invariant：pre 是已反转部分的头，cur 是未反转部分的头；先存 nxt 再改 cur.next（先读后改）。
- 复杂度：O(n) / O(1)。迭代已最优；递归版 O(n) 栈空间，长链表有递归深度问题。
- 递归版（同一次）：老毛病，`reverse(cur,nxt)` 漏了 `return`，新头只在最深层返回，中间层丢掉 → 整体返回 None。反例 [1,2]。改 `return reverse(cur,nxt)`。
- 口诀：递归的答案在最底下，每一层都要 return 把它传上来。递归版 O(n) 栈，Python 不优化尾递归。
