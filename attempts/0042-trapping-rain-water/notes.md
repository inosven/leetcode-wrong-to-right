# LC 42 Trapping Rain Water

## 2026-11-24 · B · 20min（单调栈）

- 层级：实现错 ×2。
- Bug 1（第一个出错点，老毛病：值和下标比较，同 739 第一次）：`height[i] > stack[-1]`，stack 存下标，应为 `height[stack[-1]]`。反例 [2,1,2] → 0；官方示例 → 0。
- Bug 2：一层水高度少减坑底：`min(lefth, righth) * 宽` 应为 `(min(lefth, righth) - height[mid]) * 宽`。只修 Bug 1 时 [2,1,2] → 2。
- 小点：栈空时 `lefti = i-1` 碰巧宽度为 0 加了 0；语义上没有左墙应 `break`。
- 追问：break vs continue 都只作用于 while，二者结果相同；跳过的是"算水"不是"入栈"，当前柱子必须入栈留作后面的左墙（反例 [1,2,1,2]）。
- invariant：栈存下标，对应高度递减；弹出 mid 算一层水：(矮墙 − 坑底) × 宽。
- 口诀：栈里存下标，比较先取高度；一层水 = 矮墙 − 坑底。
- 复杂度：O(n) / O(n)。改进：双指针 O(1) 空间（面试常追问）。

## 2026-11-24 · C · 15min（双指针）

- 贴上来的版本正确（官方示例 6、9；随机对拍 5000 组一致）。自评 C：双指针思路不是自己想出来的。
- 写法：比较 left_max / right_max（标准写法比较 height[left] / height[right]），两者等价：哪边墙矮先结算哪边。
- invariant：left_max <= right_max 时，left 右侧真正的最大值 ≥ right_max ≥ left_max，所以 left 这格的水只由 left_max 决定；`left <= right` 让每格恰好结算一次。
- 改进：先更新 max 再算水，差值必 ≥ 0，可去掉 `>= 0` 判断。
- 复杂度：O(n) / O(1)。
