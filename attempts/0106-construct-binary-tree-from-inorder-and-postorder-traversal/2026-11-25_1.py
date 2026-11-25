# LC 106 Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 日期: 2026-11-25 | 章节: 二叉树 | 结果: B | 用时: 10min

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        ntoi = {n:i for i,n in enumerate(inorder)}
        def build(inorder,postorder):
            root = TreeNode()
            if len(inorder) ==0:
                return None
            mid = postorder[-1]
            midpos = ntoi[mid]

            left_inorder = inorder[:mid]
            right_inorder = inorder[mid+1:]

            left_size = len(left_inorder)

            left_postorder = postorder[:left_size]
            right_porstorder = postorder[left_size:-1]
            left = build(left_inorder,left_postorder)
            right = build(right_inorder,right_inorder)
            root.left = left
            root.right = right
            return root
        return build(inorder, postorder)
