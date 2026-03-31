'''
Author: Hannah
Date: 2026-03-30 23:34:02
LastEditTime: 2026-03-30 23:46:09
'''
#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # Method: recursion
        # for each node, judge whether it is in range
        # if in range, add it into sum; otherwise, do nothing
        # after finishing one node, go to its sub-node
        # Time complexity: worst case O(N), N is the number of nodes
        # Space complexity: worst case O(N)

        if root is None:
            return 0
        # Because it's a Binary Search Tree
        s = root.val if low <= root.val <= high else 0
        # right tree might be within the range
        if root.val < high:
            s += self.rangeSumBST(root.right, low, high)
        # left tree might be within the range
        if root.val > low:
            s += self.rangeSumBST(root.left, low, high)
        
        return s
# @lc code=end

