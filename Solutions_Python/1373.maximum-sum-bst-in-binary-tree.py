'''
Author: Hannah
Date: 2026-04-06 17:57:01
LastEditTime: 2026-04-06 19:43:00
'''
#
# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
#

# @lc code=start

# from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # Method: post-order traversal
        # given a node, judge whether this sub-tree is a BTS
        # if it's a BTS, add its value to sum, continue going up
        # if it's not a BTS, the sum stops at its sub-tree
        # use a global value to record the answer
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(H); worst case H=N

        ans = 0

        # a function return the min value, max value, sum of current tree
        def dfs(node):
            if node is None:
                return inf, -inf, 0
            
            l_min, l_max, l_sum = dfs(node.left)
            r_min, r_max, r_sum = dfs(node.right)
            x = node.val
            # if the tree based on current node is not BTS
            if x <= l_max or x >= r_min:
                return -inf, inf, 0
            # if it's BTS, update ans
            s = l_sum + r_sum + x
            nonlocal ans
            ans = max(ans, s)
            return min(l_min, x), max(r_max, x), s
        
        dfs(root)

        return ans
# @lc code=end

