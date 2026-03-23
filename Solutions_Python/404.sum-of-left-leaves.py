'''
Author: Hannah
Date: 2026-03-22 20:23:43
LastEditTime: 2026-03-22 20:35:08
'''
#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # Method 2: recursion
        if root is None:
            return 0
        
        # get the max left leave sum of left node and right node
        ans = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        # if the left son of current node is left leave
        # add the value into ans
        left = root.left
        if left and left.left is None and left.right is None:
            ans += left.val
        
        return ans
    
        # Method 1: Global answer

        # a function to find
        def dfs(node):
            if node is None:
                return
            
            # find the left leave
            dfs(node.left)
            dfs(node.right)

            # left node
            left = node.left
            # if left node of current node is leave
            if left and left.left is None and left.right is None:
                nonlocal ans
                ans += left.val
            
        # update global answer
        ans = 0
        dfs(root)

        return ans
# @lc code=end

