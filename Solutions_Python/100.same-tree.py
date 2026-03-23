'''
Author: Hannah
Date: 2026-03-23 11:44:55
LastEditTime: 2026-03-23 11:51:46
'''
#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Method: recursion
        # if one of p is empty, the other is not, then tree is not the same
        # if both of them is empty, p and q is the same
        if p is None or q is None:
            return p == q
        # if p and q both has value
        # if the values are the same, check their sub-node
        if p.val == q.val:
            # if p.left = q.left, and p.right = q.right, then return True;
            # Otherwise, return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if values are not the same, it is not the same
        else:
            return False
        
# @lc code=end

