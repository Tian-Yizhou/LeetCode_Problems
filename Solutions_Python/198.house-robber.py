'''
Author: Hannah
Date: 2026-01-23 19:50:44
LastEditTime: 2026-01-23 20:21:32
'''
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0, f1 = 0, 0

        for i in range(n):
            f2 = max(f0+nums[i], f1)
            f0 = f1
            f1 = f2
        
        return f2
# @lc code=end

