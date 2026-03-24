'''
Author: Hannah
Date: 2026-03-23 19:35:13
LastEditTime: 2026-03-23 19:48:16
'''
#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        # Method: recursion

        # dfs(node, val): check whether a tree has the same value with val
        def dfs(node, val):
            # if node is empty
            if node is None:
                return True
            # if node has value
            if node.val == val:
                # check its sub node; both true, return true
                return dfs(node.left, val) and dfs(node.right, val)
            else:
                return False
        
        return dfs(root, root.val)
            
        
# @lc code=end

