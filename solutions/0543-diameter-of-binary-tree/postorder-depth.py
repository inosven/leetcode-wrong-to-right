# LC 543 Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# 后序：返回深度给父节点，经过当前节点的直径 = 左深度 + 右深度，用 nonlocal 记最大值。O(n) / O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def postorder(node):
            nonlocal ans
            if not node:
                return 0
            left_depth = postorder(node.left)
            right_depth = postorder(node.right)
            maxd = left_depth + right_depth      # 经过当前节点的最长路径（边数）
            ans = max(maxd, ans)
            return max(left_depth,right_depth)+1
        postorder(root)
        return ans
