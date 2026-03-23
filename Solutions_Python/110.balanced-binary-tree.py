'''
Author: Hannah
Date: 2026-03-23 11:45:05
LastEditTime: 2026-03-23 13:00:27
'''
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Method: recursion
        
        # dfs returns the height of current node
        def dfs(node):
            # if node is None, there is no height for current node
            if node is None:
                return 0
            
            # if the sub-node of current node is None, the height is 1
            if node.left is None and node.right is None:
                return 1
            
            # Otherwise, the height of current node is the largest 
            # height of its sub-node, add 1 (itself)
            left_height = dfs(node.left)
            # trick: since min height is 0, we can use -1 to represent illegal
            # if one sub-node is illegal, we don't need to dive deep
            if left_height == -1:
                return -1
            # same for the right
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            # judge whether current node is legal
            # if it is illegal, current tree is not blanced
            if abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        # if the heihgt of root is -1, means tree is not balanced
        return dfs(root) != -1
        
# @lc code=end

