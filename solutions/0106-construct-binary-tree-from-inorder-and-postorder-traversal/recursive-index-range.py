# LC 106 Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 传区间（左闭右开）+ 全局 ntoi：中序 [左][根][右]，后序 [左][右][根]。
# 左：中序 [inl, midpos)、后序 [pol, pol+size)；右：中序 [midpos+1, inr)、后序 [pol+size, por-1)。O(n) / O(h)

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
            size = midpos-inl
            left = build(inl,midpos,pol,size+pol)
            right = build(midpos+1,inr,size+pol, por-1)
            root.left = left
            root.right = right
            return root
        return build(0,n,0,n)
