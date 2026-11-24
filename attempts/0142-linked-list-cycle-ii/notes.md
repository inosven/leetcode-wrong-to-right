# LC 142 Linked List Cycle II

## 2026-11-17 · B · 10min

- 层级：实现错。找入口的第二段（head 和相遇点同步走）正确，错在判环。
- Bug 1（第一个出错点）：`while fast.next` 没判 `fast` 本身。反例 `[1,2]` 无环：`fast` 走到 None 后取 `None.next` → AttributeError；`[]` 直接崩。老毛病：guard 要护住 `fast.next.next` 需要的 `fast` 和 `fast.next`。
- Bug 2：`if slow is not fast` 判无环。两指针初始就相等，`[1]` 不进循环 → 被当成有环，返回节点 1。
- Bug 3：`return -1` 应为 `return None`。
- 修改：`while fast and fast.next`；退出后 `if not fast or not fast.next: return None`。
- invariant：循环只有两个出口（break = 相遇有环 / 条件不成立 = fast 到头无环），看退出条件区分。
- 口诀：`x.next.next` 前 `x` 和 `x.next` 都判空；判断从哪个出口退出，看退出条件，不看初始就成立的状态。

## 2026-11-23 · B · 10min

- 层级：实现错。上次判环的三个 bug 这次都没犯；这次错在第二段找入口：`while True` 里先走再比较，入口就是 head（a = 0）时第 0 步的相等被跳过。
- 反例 [1,2] pos=0：相遇点 = 节点 1 = 入口，先走一步后两者都在 2 → 返回 2。穷举长度 0–8：pos=0 且 n ≥ 2 全错，[1] 自环碰巧对。
- 修改：`while p != slow: 走一步`，循环外 `return p`。
- invariant：同步走 k 步后两者离入口都是 a − k，相等可能出现在 k = 0。
- 口诀：先比较再走，第 0 步也要检查。
- 复杂度：O(n) / O(1)。改进：节点比较用 `is`。
