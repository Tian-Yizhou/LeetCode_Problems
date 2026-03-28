'''
Author: Hannah
Date: 2026-03-27 19:16:57
LastEditTime: 2026-03-27 19:30:20
'''
#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Method: recursion
        # given node1 and node2,
        # if both nodes are not None, sum them;
        # Otherwise, keep the node that is not None.
        # if both nodes are None, return None
        # after dealing with these two root nodes, apply the function to their sub-nodes
        
        # merge nodes to tree 1
        if root1 is None and root2 is None:
            return None
        else:
            if root1 is None and root2 is not None:
                return root2
            elif root1 is not None and root2 is None:
                return root1
            else:
                # merge the value of two roots
                root1.val = root1.val + root2.val
                # apply the funtion to their sub-nodes
                # because we need to merge nodes to tree 1
                root1.left = self.mergeTrees(root1.left, root2.left)
                root1.right = self.mergeTrees(root1.right, root2.right)
                return root1
# @lc code=end

