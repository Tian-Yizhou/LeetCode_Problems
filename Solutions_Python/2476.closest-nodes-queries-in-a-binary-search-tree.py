'''
Author: Hannah
Date: 2026-03-31 21:46:23
LastEditTime: 2026-04-01 22:39:50
'''
#
# @lc app=leetcode id=2476 lang=python3
#
# [2476] Closest Nodes Queries in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # if there is a node with value query[i], then min_i and max_i are this value

        # Method 2: use Binary Search Tree in-order traversal + bisect
        # Time complexity: O(N+qlogN). scan each node once, plus q times bisect
        # Space complexity: O(N). the increasing array, plus the space for ans

        # a function to construct an increasing array
        a = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
        dfs(root)

        # a bisect function to find the idx of first value that >= target val
        def my_bisect(nums, target):
            n = len(nums)
            # open interval
            left, right = -1, n
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            return right
        
        ans = []
        n = len(a)
        for q in queries:
            # find the idx whose value first >= target
            idx = my_bisect(a, q)
            # if there is such a value in array
            if idx < n:
                max_i = a[idx]
            # otherwise, no such value
            else:
                max_i = -1
            # if no max_i, or the value is not q
            if idx == n or a[idx] != q:
                # move idx to its left
                idx -= 1
            # if idx is still within the range, we can find min_i
            if idx >= 0:
                min_i = a[idx]
            # otherwise, no such min_i
            else:
                min_i = -1
            ans.append([min_i, max_i])
        
        return ans

        # Method 1: correct but Time Limit Exceeded
        def find_min_i(node, val, min_i):
            if node is None:
                return min_i
            if node.val == val:
                return val
            # if node value > val, possible answer is in left tree
            elif node.val > val:
                return find_min_i(node.left, val, min_i)
            else:
                min_i = max(min_i, node.val)
                return find_min_i(node.right, val, min_i)
        
        def find_max_i(node, val, max_i):
            if node is None:
                return max_i
            if node.val == val:
                return val
            # if node value > val, possible answer is in left tree
            elif node.val > val:
                max_i = node.val if max_i == -1 else min(max_i, node.val)
                return find_max_i(node.left, val, max_i)
            else:
                return find_max_i(node.right, val, max_i)
        
        ans = []

        for val in queries:
            min_i = find_min_i(root, val, -1)
            max_i = find_max_i(root, val, -1)
            ans.append([min_i, max_i])
        
        return ans

# @lc code=end

