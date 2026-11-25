# LeetCode (Python 3)

**English** | [中文](README.zh-CN.md)

- `solutions/`: a correct solution for each problem; one file per distinct approach.
- `attempts/`: every submitted version as written, including wrong ones, plus `notes.md` with the review of each attempt (in Chinese). Append-only.

Result: A = solved independently · B = right idea, but with bugs · C = no idea

| # | Problem | Topic | Attempts | History | Solution |
|---|---|---|---|---|---|
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers | 1 | 11-17 B | [sort-two-pointers](solutions/0015-3sum/sort-two-pointers.py) |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | Two Pointers | 1 | 11-17 A | [sort-two-pointers](solutions/0018-4sum/sort-two-pointers.py) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Linked List | 2 | 11-14 A, 11-19 A | [fast-slow-pointers](solutions/0019-remove-nth-node-from-end-of-list/fast-slow-pointers.py) |
| 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Backtracking | 1 | 11-19 A | [backtracking](solutions/0040-combination-sum-ii/backtracking.py) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Monotonic Stack | 2 | 11-24 B, 11-24 C | [monotonic-stack](solutions/0042-trapping-rain-water/monotonic-stack.py), [two-pointers](solutions/0042-trapping-rain-water/two-pointers.py) |
| 59 | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | Array | 1 | 11-17 A | [shrink-boundaries](solutions/0059-spiral-matrix-ii/shrink-boundaries.py) |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic Stack | 2 | 11-24 C | [monotonic-stack](solutions/0084-largest-rectangle-in-histogram/monotonic-stack.py) |
| 106 | [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Binary Tree | 1 | 11-17 B | [recursive-slicing](solutions/0106-construct-binary-tree-from-inorder-and-postorder-traversal/recursive-slicing.py) |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Backtracking | 2 | 11-19 B, 11-21 B | [backtracking](solutions/0131-palindrome-partitioning/backtracking.py) |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Greedy | 1 | 11-19 A | [greedy](solutions/0134-gas-station/greedy.py) |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Linked List | 2 | 11-17 B, 11-23 B | [floyd-fast-slow](solutions/0142-linked-list-cycle-ii/floyd-fast-slow.py) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Linked List | 4 | 11-23 C, 11-24 A | [array-two-pointers](solutions/0143-reorder-list/array-two-pointers.py), [reverse-second-half](solutions/0143-reorder-list/reverse-second-half.py) |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack & Queue | 2 | 11-14 B, 11-19 B | [stack](solutions/0150-evaluate-reverse-polish-notation/stack.py) |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | String | 2 | 11-19 B, 11-21 B | [reverse-twice](solutions/0151-reverse-words-in-a-string/reverse-twice.py) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List | 2 | 11-23 B | [iterative](solutions/0206-reverse-linked-list/iterative.py), [recursive](solutions/0206-reverse-linked-list/recursive.py) |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Array | 1 | 11-19 A | [sliding-window](solutions/0209-minimum-size-subarray-sum/sliding-window.py) |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Stack & Queue | 6 | 11-17 C, 11-19 C, 11-20 B | [two-stack](solutions/0224-basic-calculator/two-stack.py), [sign-stack](solutions/0224-basic-calculator/sign-stack.py) |
| 236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Binary Tree | 2 | 11-17 B, 11-23 A | [recursive-postorder](solutions/0236-lowest-common-ancestor-of-a-binary-tree/recursive-postorder.py) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Dynamic Programming | 1 | 11-20 B | [dp-2d](solutions/0322-coin-change/dp-2d.py), [dp-1d](solutions/0322-coin-change/dp-1d.py) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Stack & Queue | 1 | 11-17 B | [count-buckets](solutions/0347-top-k-frequent-elements/count-buckets.py), [sort-by-count](solutions/0347-top-k-frequent-elements/sort-by-count.py) |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Dynamic Programming | 2 | 11-17 B | [dp-2d](solutions/0416-partition-equal-subset-sum/dp-2d.py), [dp-1d](solutions/0416-partition-equal-subset-sum/dp-1d.py) |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Greedy | 1 | 11-19 A | [greedy-sort-by-start](solutions/0452-minimum-number-of-arrows-to-burst-balloons/greedy-sort-by-start.py) |
| 454 | [4Sum II](https://leetcode.com/problems/4sum-ii/) | Hash Table | 2 | 11-14 A, 11-19 A | [hashmap-pair-sums](solutions/0454-4sum-ii/hashmap-pair-sums.py) |
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Monotonic Stack | 3 | 11-14 B, 11-19 B, 11-19 A | [monotonic-stack](solutions/0496-next-greater-element-i/monotonic-stack.py) |
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Monotonic Stack | 1 | 11-19 A | [monotonic-stack-two-pass](solutions/0503-next-greater-element-ii/monotonic-stack-two-pass.py) |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Graph | 2 | 11-19 B, 11-21 B | [dfs-stack](solutions/0695-max-area-of-island/dfs-stack.py), [dfs-recursive](solutions/0695-max-area-of-island/dfs-recursive.py), [dfs-recursive-inplace](solutions/0695-max-area-of-island/dfs-recursive-inplace.py) |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Monotonic Stack | 3 | 11-14 C, 11-21 A, 11-24 A | [monotonic-stack](solutions/0739-daily-temperatures/monotonic-stack.py), [right-to-left-jump](solutions/0739-daily-temperatures/right-to-left-jump.py) |
| 772 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) (Premium) | Stack & Queue | 4 | 11-17 C, 11-19 C, 11-20 B | [two-stack](solutions/0772-basic-calculator-iii/two-stack.py) |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Dynamic Programming | 2 | 11-17 C, 11-19 A | [dp-2d](solutions/1143-longest-common-subsequence/dp-2d.py) |
