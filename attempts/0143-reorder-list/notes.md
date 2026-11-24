# LC 143 Reorder List

## 2026-11-23 · C · 25min（三版）

- 最初想法：先建一条 reversed list，再左右指针直到 左 == 右。问题：原地反转会丢掉正序；复制新链表节点不是同一批，`==` 永远不成立；偶数长度左右会交错而不相遇；尾节点要置 None。
- 第 1 版（节点存数组 + 左右下标）：思路对，收尾两处错，都会成环。
  - 奇数长度最后 left == right 时同一节点接两次 → `[1]` 自环。加 `if left > right: break`。
  - 尾节点 .next 没断 → `[1,2,3,4]` 中 3.next 仍是 4。循环后 `cur.next = None`。
  - 口诀：重排链表最后一步把尾节点 .next 置 None；左右相遇的那个节点只接一次。
- 第 2 版（找中点 + 反转后半段 + 合并）：merge 只接了 head1 → head2，漏了 `head2.next = nxt1` → 成环。口诀：交替合并每轮改两根指针。
- 第 3 版：补上后正确。
- 改进：拆分是碰巧对的（reverse(mid) 让 mid 同时在两段里，`mid.next = None` 是空操作）；应先断开再反转：`second = mid.next; mid.next = None; reverse(second)`。
- 复杂度：数组版 O(n) / O(n)；反转后半段版 O(n) / O(1)。
