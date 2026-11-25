# LC 543 Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# 日期: 2026-11-25 | 章节: 二叉树 | 结果: C | 用时: 15min

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # maxd 经过当前节点的最长距离
        ans = 0
        def postorder(node):
            nonlocal ans
            if not node:
                return 0
            left_depth = postorder(node.left)
            right_depth = postorder(node.right)
            maxd = left_depth + right_depth
            ans = max(maxd, ans)
            return max(left_depth,right_depth)+1
        _ = postorder(root)
        return ans
