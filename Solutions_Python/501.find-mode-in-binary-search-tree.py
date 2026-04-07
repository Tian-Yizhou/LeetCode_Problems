'''
Author: Hannah
Date: 2026-04-05 21:23:41
LastEditTime: 2026-04-06 17:36:28
'''
#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node, lst):
        if node is None:
            return
        self.inOrder(node.left, lst)
        lst.append(node.val)
        self.inOrder(node.right, lst)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        # Method 2: in-ortder traversal
        # only scan the tree once
        self.ans = []
        self.pre = None
        self.cnt = 0
        self.max_cnt = 0

        def dfs(node):
            if node is None:
                return
            # left tree
            dfs(node.left)
            # root node
            if node.val == self.pre:
                self.cnt += 1
            else:
                self.cnt = 1
                self.pre = node.val

            if self.cnt == self.max_cnt:
                self.ans.append(node.val)
            elif self.cnt > self.max_cnt:
                self.max_cnt = self.cnt
                self.ans = [node.val]
            # right tree
            dfs(node.right)
        
        dfs(root)

        return self.ans

        # Method 1: in-order traversal
        # Because it's Binary Search Tree, in-order traversal gives us a non-decreasing sequence
        # We can convert the tree in to a array first

        # a list to store the value of i-th node, covert the tree to a ordered array
        lst = []
        self.inOrder(root, lst)
        # the value of previous node
        pre = lst[0]
        # record the count of current value
        cnt = 1
        # the max count
        max_cnt = 1
        # initialize answer
        ans = [lst[0]]

        # go through the array, find the mode
        for i in range(1, len(lst)):
            # if current value equals previous value
            if pre == lst[i]:
                # update cnt
                cnt += 1
            else:
                cnt = 1
            # if a value's count equals max count, add it into ans
            if cnt == max_cnt:
                ans.append(lst[i])
            # if max_cnt is exceeded, update max count and ans
            if cnt > max_cnt:
                max_cnt = cnt
                # reset ans
                ans = [lst[i]]
            pre = lst[i]

        return ans
    
# @lc code=end

