'''
Author: Hannah
Date: 2026-03-22 20:58:49
LastEditTime: 2026-03-22 21:17:51
'''
#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # Method 2: recursion
        # if use this method, we need to add cur_sum as a parameter into sumNumbers
        # Other parts are similar

        # Method 1: Global variable
        ans = 0
        # function to add value
        def dfs(node, cur_sum):
            # if it is empty, don't do anything
            if node is None:
                return
            
            # if it is a node with value, update cur_sum
            cur_sum = cur_sum*10 + node.val

            # if it is a leaf, update value
            if node.left is None and node.right is None:
                nonlocal ans
                ans += cur_sum
            
            # pass the cur_sum to sub_node
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
        
        # call the function to get answer
        dfs(root, 0)
        
        return ans

# @lc code=end

