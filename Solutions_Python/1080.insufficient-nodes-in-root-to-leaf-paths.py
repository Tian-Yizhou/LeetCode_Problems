'''
Author: Hannah
Date: 2026-03-28 14:18:22
LastEditTime: 2026-03-28 14:48:45
'''
#
# @lc app=leetcode id=1080 lang=python3
#
# [1080] Insufficient Nodes in Root to Leaf Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        # Method: recursion, dfs
        # bottom to top: when reach a leaf node, judge whether sum < limit
        # if sum < limit, delete the leaf node; Otherwise, keep it.
        # For a non-leaf node, if all children of a non-leaf node are deleted,
        # then it also should be deleted
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(H), H is the height of the tree. Worst case: H = N

        def dfs(node, s):
            # if achieve the end, return True if s < limit
            if node is None:
                return None
            # if it's a node
            else:
                # update s
                s += node.val

                # if it's leaf node:
                if node.left is None and node.right is None:
                    return None if s < limit else node
                
                # if it's non-leaf node:
                # if both of its children under the limit, delete this node (return None)
                # Otherwise, keep this node (return itself)
                node.left = dfs(node.left, s)
                node.right = dfs(node.right, s)
                if node.left is None and node.right is None:
                    return None
                else:
                    return node

        return dfs(root, 0)

# @lc code=end

