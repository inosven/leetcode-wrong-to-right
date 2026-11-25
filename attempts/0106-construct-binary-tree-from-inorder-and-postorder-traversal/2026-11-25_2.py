# LC 106 Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 日期: 2026-11-25 | 章节: 二叉树 | 结果: B | 用时: 10min（传区间版）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        ntoi = {n:i for i,n in enumerate(inorder)}
        n = len(inorder)
        def build(inl,inr,pol,por):
            if inl==inr:
                return None
            
            mid = postorder[por-1]
            midpos = ntoi[mid]
            root = TreeNode(val=mid)
            size = mid-inl
            left = build(inl,midpos,pol,size+pol)
            right = build(midpos+1,inr,size+pol+1, por-1)
            root.left = left
            root.right = right
            return root
        return build(0,n,0,n)
