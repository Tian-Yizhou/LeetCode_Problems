'''
Author: Hannah
Date: 2026-03-22 20:02:26
LastEditTime: 2026-03-22 20:13:03
'''
#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # Method: recursion

        # if root is None
        if root is None:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # if left node is None, we must go to the right
        if root.left is None:
            return right_depth + 1
        # if right node is None, we must go to the left
        if root.right is None:
            return left_depth + 1
        
        # if both sub-node are not None
        return min(left_depth, right_depth) + 1

        
# @lc code=end

