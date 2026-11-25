# LC 84 Largest Rectangle in Histogram

## 2026-11-24 · C · 15min（两版）

- 第 1 版：实现错 ×2。
  - Bug 1（第一个出错点）：哨兵只加一半：`stack = [0]` 但 heights 开头没补 0，下标 0 是真柱子且被 push 两次，弹完栈空 → `stack[-1]` IndexError。反例 [1]；官方示例也 IndexError。
  - Bug 2：矩形高用了 `heights[i]`（右边界），应为 `heights[midpos]`（被弹出的柱子）。
- 第 2 版：heights 两头补 0、高改对，但 `stack = []` 且循环从 1 开始 → 左哨兵下标 0 从未入栈，`[2,1]` IndexError。改 `stack = [0]`。
- invariant：栈存下标，高度递增；弹出 midpos 时，右边界是第一个比它矮的 i，左边界是新栈顶；0 哨兵永不弹出。
- 口诀：谁被弹出就以谁为高；哨兵要两头都到位：数组里有值，栈里有位置。
- 复杂度：O(n) / O(n)。改进：不改输入用 `h = [0] + heights + [0]`；或不要左哨兵，`leftpos = stack[-1] if stack else -1`。
- 追问：没有像 LC 42 那样的双指针。面积取决于区间内的最小值，不只看两端，左右收缩无法判断该丢哪一边；LC 11 盛水只看两端才能双指针。替代解法：分治 O(n log n)，或用"跳跃"预处理每根柱子左右第一个更矮的位置。
