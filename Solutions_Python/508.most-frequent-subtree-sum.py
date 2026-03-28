'''
Author: Hannah
Date: 2026-03-27 19:38:56
LastEditTime: 2026-03-27 20:09:30
'''
#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start

# from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        # Method: recursion
        # define a function to count the sum of all subtree,
        # return a hash map, key: sum value, value: count
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(N). The worst case is each subtree sum is unique, then use O(N); and the space for recursion stack, averagely is O(logN), worst case O(N)

        # special case
        if not root:
            return []
            
        cnt = Counter()
        max_cnt = 0
        
        def get_sum(node):
            nonlocal max_cnt

            if not node:
                return 0
            
            # use recursion to get the sum of sub-tree
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            # update hash map
            cnt[current_sum] += 1
            # update max sum count
            max_cnt = max(max_cnt, cnt[current_sum])
            
            return current_sum
        
        # apply to the root
        get_sum(root)
        
        # find all sum that equal max_cnt
        return [s for s, freq in cnt.items() if freq == max_cnt]



            
# @lc code=end

