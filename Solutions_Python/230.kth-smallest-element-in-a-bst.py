'''
Author: Hannah
Date: 2026-04-06 17:37:45
LastEditTime: 2026-04-06 17:56:41
'''
#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Method: in-order traversal
        # Because it's a Binary Search Tree, we can get an non-decreasing sequence
        # Time complexity: O(H+k). Worst case O(N), N is the number of nodes
        # Space complexity: O(H), worst case H=N
        self.k_cnt = 0
        self.ans = inf

        # a function to find the k-th smallest value
        def dfs(node):
            if node is None:
                return
            
            # left tree
            dfs(node.left)
            # current root node
            if self.k_cnt < k:
                self.k_cnt += 1
                if self.k_cnt == k:
                    self.ans = node.val
                    return
            # right tree
            dfs(node.right)
        
        dfs(root)

        return self.ans

# @lc code=end

