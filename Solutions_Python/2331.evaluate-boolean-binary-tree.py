'''
Author: Hannah
Date: 2026-03-27 19:30:46
LastEditTime: 2026-03-27 19:38:38
'''
#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        # Method: recursion
        # we can find that none-leaf nodes have sub-nodes, 
        # while leaf nodes don't have sub-nodes
        # given a root node, 
        # if it's non-leaf, apply the funciton to its sub-nodes;
        # if it's leaf, return boolean

        # if the node is leaf
        if root.val == 0 or root.val == 1:
            if root.val == 0:
                return False
            else:
                return True
        #  if the node is non-leaf
        else:
            # OR operation
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            # AND operation
            else:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)

# @lc code=end

