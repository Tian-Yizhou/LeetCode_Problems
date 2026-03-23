'''
Author: Hannah
Date: 2026-03-22 21:18:25
LastEditTime: 2026-03-23 11:33:17
'''
#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start

# from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Method 2
        # record min col, avoid sorting by col number
        groups = defaultdict(list)
        min_col = 0
        # func to extract information, with updating min_col
        def dfs(node, row, col):
            if node is None:
                return
            nonlocal min_col
            min_col = min(min_col, col)
            groups[col].append((row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root, 0, 0)

        ans = []
        for col in range(min_col, min_col+len(groups)):
            g = groups[col]
            # we still need to sort by (row, val)
            g.sort()
            ans.append([val for _, val in g])
        
        return ans


        # Method 1
        # a hash map, value is list
        groups = defaultdict(list)

        # a function to extract the information of given node
        def dfs(node, row, col):
            """
            Parameters
            ----------
            row : row number of current node
            col : column number of current node
            """
            # if node is empty, return function
            if node is None:
                return
            # if node has a value, get its information
            groups[col].append((row, node.val))
            # applay this funtion to its sub-node
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        # apply dfs to root, then we get information of all nodes in dict
        dfs(root, 0, 0)

        # construct answer
        ans = []
        # for each group in groups, sorted by col number
        for _, g in sorted(groups.items()):
            # for the value in the same col, sort by row, value
            g.sort()
            # update ans
            ans.append([val for _, val in g])
        
        return ans
# @lc code=end

