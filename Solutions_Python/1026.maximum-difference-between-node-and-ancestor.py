'''
Author: Hannah
Date: 2026-03-28 12:31:53
LastEditTime: 2026-03-28 13:17:16
'''
#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
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

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        # Method: recursion, up to bottom
        # given a node, update max and min ancestor (include itself),
        # pass max and min ancestors to its children.
        # do calculation to get the answer when node is None (end of the tree)
        # Time complexity: O(N), N is the number of all nodes. Each node is use only once, and cost time O(1)
        # Space Complexity: O(H), H is the height of whole tree, because the call stack of recursion
        
        # function to update answer
        def dfs(node, min_ancestor, max_ancestor):
            if node is None:
                return max_ancestor - min_ancestor
            
            # update the current max and min value on current path
            min_ancestor = min(min_ancestor, node.val)
            max_ancestor = max(max_ancestor, node.val)
            
            # apply this function to its children
            left_diff = dfs(node.left, min_ancestor, max_ancestor)
            right_diff = dfs(node.right, min_ancestor, max_ancestor)
            
            return max(left_diff, right_diff)

        # apply dfs to root
        return dfs(root, root.val, root.val)

# @lc code=end

