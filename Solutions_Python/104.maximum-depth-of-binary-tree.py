'''
Author: Hannah
Date: 2026-03-22 19:55:09
LastEditTime: 2026-03-22 20:02:13
'''
#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Method 2: use global variable
        ans = 0

        # function to get the depth of given node
        # cnt is the depth to achieve node
        def cnt_depth(node, cnt):
            # if there is no node, we finish counting
            if node is None:
                return
            # otherwise, depth + 1
            cnt += 1
            # update global variable ans
            nonlocal ans
            ans = max(ans, cnt)
            # search sub node
            cnt_depth(node.left, cnt)
            cnt_depth(node.right, cnt)
        
        # find the depth for root
        cnt_depth(root, 0)

        return ans

            
        # Method 1: recursion
        # if node is none, return 0
        if root is None:
            return 0
        
        ans = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return ans
        
# @lc code=end

