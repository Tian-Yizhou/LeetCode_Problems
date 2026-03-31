#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # Method: recursion
        # Because it's a BTS, the gap between any node in right tree and 
        # any node in left tree, will definitely greater than the gap 
        # between two nodes in the same tree
        # we need 3 gaps: 
        # the min gap between root and its two sub-nodes;
        # the min gap in left tree; the min gap in right tree
        # we can use in-order traversal: left->root->right

        ans = inf
        pre = -inf

        def dfs(node):
            # if node is None, do nothing
            if node is None:
                return
            # if node has a value
            # check left tree first
            dfs(node.left)
            nonlocal ans, pre
            # update answer and previous node value
            ans = min(ans, node.val - pre)
            pre = node.val
            # check right tree
            dfs(node.right)
        
        dfs(root)

        return ans
            

# @lc code=end

