'''
Author: Hannah
Date: 2026-03-22 21:18:18
LastEditTime: 2026-03-22 21:31:43
'''
#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Method 2: recursion
        # if we use recursion, we need to add cur_max as a new parameter into goodNodes()
        
        # the number of good nodes of current node is
        # good nodes on its sub-node + 1 (if itself is good node)

        
        # Method 1: Global variable

        # maintain the max value of current path
        def dfs(node, cur_max):
            # if node is empty, do nothing
            if node is None:
                return
            # if node has a value, judge whether the node is good
            if node.val >= cur_max:
                # update max value in this path
                cur_max = node.val
                # update ans
                nonlocal ans
                ans += 1
            # apply this function to its sub-node
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
        
        ans = 0
        # apply dfs to root
        dfs(root, root.val)

        return ans

            
# @lc code=end

