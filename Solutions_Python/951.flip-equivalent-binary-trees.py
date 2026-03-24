#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # the root node of two tree should be the same
        # if either node is None
        if root1 is None or root2 is None:
            return root1 == root2
        # if both nodes has value
        if root1.val == root2.val:
            # their sub-node should be either the same or flip equivalant
            if_same = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            if_flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            return if_same or if_flip
        else:
            return False
# @lc code=end

