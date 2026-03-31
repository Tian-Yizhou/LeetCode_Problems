'''
Author: Hannah
Date: 2026-03-30 23:17:55
LastEditTime: 2026-03-30 23:33:47
'''
#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Method: recursion
        # Since it's a Binary Search Tree,
        # if val > root.val, we should search right tree;
        # if val < root.val, we should search left tree;
        # if val == root.val, we find the tree
        # Time complexity: O(H), H is the height of the tree. Worst case H=N; best case H=1
        # Space complexity: O(H)

        if not root or root.val == val:
            return root
    
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# @lc code=end

