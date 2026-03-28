'''
Author: Hannah
Date: 2026-03-28 13:17:37
LastEditTime: 2026-03-28 14:17:59
'''
#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        # Method: recursion, dfs
        # given a node, we have two operation methods
        # 1. next step go to the inverse direction w.r.t its direction to its parents
        # 2. next step go to the same direction w.r.t its direction to its parents (start from new node)
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(H), H is the height of tree. If balanced binary tree, H = logN; worst case H = N

        # function to get the max path length of current node
        def dfs(node, length, isLeft):
            # if achieve the end
            if node is None:
                return
            else:
                # update the longest length
                self.ans = max(self.ans, length)
                # if current node is the left node of its parent (isLeft=True)
                # then it's a new start; Otherwise, continue zig-zag
                dfs(node.left, 1 if isLeft else length+1, True)
                # if current node is the right node of its parent (isLeft=False)
                # same logic
                dfs(node.right, length+1 if isLeft else 1, False)
        
        # set ans, start from 0 (if there is only one node)
        self.ans = 0
        dfs(root, 0, True)

        return self.ans
    
# @lc code=end

