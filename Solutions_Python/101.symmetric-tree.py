'''
Author: Hannah
Date: 2026-03-23 11:44:59
LastEditTime: 2026-03-23 12:45:35
'''
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # 100. is same tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if node p or node q is empty, only return true if both are empty
        if p is None or q is None:
            return p == q
        # when p and q both have value
        # if p.val = q.val, we need to check whether their sub node is the same
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if p.val != q.val, they are not the same, return False
        else:
            return False

    # function to judge whether two tree are symmetric
    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if two root nodes are empty, return true only when they're both empty
        if p is None or q is None:
            return p == q
        
        # if they have the same value
        if p.val == q.val:
            # left node of p should be the same with right node of q
            return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Method: recursion
        # given a node, judge whether its left tree and right tree are symmetric
        # it's the similar logic in problem 100. is same tree
        # see function isMirrot()

        return self.isMirror(root.left, root.right)

# @lc code=end

