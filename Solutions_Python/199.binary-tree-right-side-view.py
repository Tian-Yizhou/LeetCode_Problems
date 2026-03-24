'''
Author: Hannah
Date: 2026-03-23 13:02:21
LastEditTime: 2026-03-23 13:35:23
'''
#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Method: recursion
        
        # check right sub-tree first, record the depth
        # if depth has gone beyond record(answer length)
        # add it into answer

        ans = []

        # a function to check the depth of current node and record
        # depth is passed by previous nodes
        def dfs(node, depth):
            # if node is empty, do nothing
            if node is None:
                return
            # update answer
            if len(ans) == depth:
                ans.append(node.val)
            
            # if current node has sub-node
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        # apply dfs to root
        dfs(root, 0)
        
        return ans

# @lc code=end

