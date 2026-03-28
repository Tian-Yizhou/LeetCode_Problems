'''
Author: Hannah
Date: 2026-03-23 21:00:26
LastEditTime: 2026-03-27 19:16:27
'''
#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Method: recursion
        # given a node, if its sub-nodes are not both None,
        # inverse its sub-nodes; Otherwise, keep it as is

        if root is None:
            return root

        if root.left is None and root.right is None:
            return root
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
# @lc code=end

