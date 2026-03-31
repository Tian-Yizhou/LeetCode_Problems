'''
Author: Hannah
Date: 2026-03-30 22:20:03
LastEditTime: 2026-03-30 23:16:54
'''
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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

    pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Method 3: recursion, post-order traversal
        # if our path is left->right->root, 
        # the value of node should be greater than the max value of its left tree
        # and should be less than the min value of right tree
        # note we need the min and max of left tree and min and max of right tree
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(N)
        
        return self.check_3(root)[1] != inf
        
        # Method 2: recursion, in-order traversal
        # if our path is left->root->right, we should get a strictly increasing array
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(N)
        return self.check_2(root)
        
        # Method 1: recursion, pre-order traversal
        # given a node as root, judge whether it's a BST
        # Time complexity: O(N), N is the number of nodes. For each node, check whether its value is within the range
        # Space complexity: O(N)
        
        # apply check to root
        return self.check_1(root, -inf, inf)
    
    def check_3(self, node):

        # note: here the return is inf, -inf, to handle invalid case
        if node is None:
            return inf, -inf
        
        l_min, l_max = self.check_3(node.left)
        if node.val <= l_max:
            return -inf, inf
        r_min, r_max = self.check_3(node.right)
        if node.val >= r_min:
            return -inf, inf
        
        return min(l_min, node.val), max(r_max, node.val)
    
    def check_2(self, node):
        # the value of node should be greater than last_val
        if node is None:
            return True
        # check its left tree
        if not self.check_2(node.left):
            return False
        # check the node itself
        if node.val <= self.pre:
            return False
        # check its right tree
        else:
            self.pre = node.val
            return self.check_2(node.right)

    def check_1(self, node, lower_b, upper_b):

        if node is None:
            return True
        
        # condition: the node value should in the range
        if lower_b < node.val < upper_b:
            # and its left tree, right tree should also be BTS
            return self.check_1(node.left, lower_b, node.val) and self.check_1(node.right, node.val, upper_b)
        else:
            return False
        
# @lc code=end

