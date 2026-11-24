# LC 236 Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 日期: 2026-11-23 | 章节: 二叉树 | 结果: A | 用时: 10min

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorder(node):
            if not node or node == p or node ==q: 
                return node
            left = postorder(node.left)
            right = postorder(node.right)

            if left and right:
                return node
            if left or right:
                return left or right
            elif not left and not right:
                return None
        return postorder(root)
