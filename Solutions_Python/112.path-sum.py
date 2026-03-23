'''
Author: Hannah
Date: 2026-03-22 20:35:49
LastEditTime: 2026-03-22 20:57:07
'''
#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False
        
        targetSum -= root.val

        # if current node is a leave
        if root.left is None and root.right is None:
            return targetSum == 0
        
        # if current node is not leave and not empty
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# @lc code=end

