# LC 543 Diameter of Binary Tree

## 2026-11-25 · C · 15min

- 贴上来的版本正确。自评 C：思路没自己想出来。
- 模式：返回值（深度）传给父节点，答案（直径 = 左深度 + 右深度）用 nonlocal 顺手记。根的返回值没人用是正常的。同类：LC 124、687。
- 改进：`_ = postorder(root)` 直接写 `postorder(root)`；注释挪到 maxd 那行。不想用 nonlocal 可返回 (深度, 子树内最大直径) 二元组，但更绕。
- 复杂度：O(n) / O(h)。
