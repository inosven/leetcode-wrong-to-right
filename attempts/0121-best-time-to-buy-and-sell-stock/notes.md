# LC 121 Best Time to Buy and Sell Stock

## 2026-11-25 · B · 15min（单机版，做过）

- 层级：定义错。持有状态从 `dp[i-1][0] - prices[i]` 转移 → 允许多次交易（变成 LC 122）。反例 [1,2,1,2] → 2（应为 1）；官方示例 → 7（应为 5）。
- 修改：`dp[i][1] = max(dp[i-1][1], -prices[i])`。
- 口诀：只能买一次，买入就从 0 起算；能买多次，才从昨天的利润起算。
- 复杂度：O(n) / O(n)；改进：压成两个变量 O(1)，或贪心 min_price（并行版的基础）。
- 数据放大：几亿条价格 → 分块并行，每块 (min, max, best)，按顺序合并（Zoox 内推人给的真题，下一步教）。

## 2026-11-26 · 讲解 · 并行版（第一次，不计成绩）

- 教学顺序：先写 merge（对）→ 讲 ProcessPoolExecutor.map（结果保序）、GIL（纯计算线程不加速）、函数须在模块顶层可 pickle、`__main__` 保护 → Quan 自己拼。
- 拼装版的问题：
  1. 函数嵌在 class Solution 里：`__main__` NameError，且无法 pickle。并行版是独立脚本，不是 LeetCode 提交。
  2. summarize 定义错：`high - low` 不管先后，[5,1] → 4（应 0）。块内利润 = 今天价 − 今天之前最低价；high 只给 merge 用。
  3. 切块：`wokers` 拼写；最后一块 `[start:start+res]` 丢数据，应 `[start:]`；len < workers 未处理 → `workers = min(workers, len)`。
  4. 没用进程池（顺序 for 循环）。
  5. merged 未初始化（应从 summaries[0] 开始）；返回了不存在的变量（应 merged[2]）。
- 口诀：摘要里的最高价只给合并用；块内利润必须"今天卖减今天之前的最低价"。
- 下次：隔几天脱稿重写，那次记成绩。
