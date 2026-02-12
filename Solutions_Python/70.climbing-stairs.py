'''
Author: Hannah
Date: 2026-01-23 20:23:14
LastEditTime: 2026-01-23 20:29:42
'''
#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        f0, f1 = 1, 1
        for i in range(1, n):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        
        return f1

        
# @lc code=end

