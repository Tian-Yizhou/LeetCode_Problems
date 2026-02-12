'''
Author: Hannah
Date: 2026-01-23 20:54:57
LastEditTime: 2026-01-23 21:25:43
'''
#
# @lc app=leetcode id=3693 lang=python3
#
# [3693] Climbing Stairs II
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # from end to the begining
        @cache
        def dp(j):
            if j <= 0:
                return 0
            else:
                res = min(dp(j-1)+1, dp(j-2)+4, dp(j-3)+9) + costs[j-1]
                return res
        
        return dp(n)


        # from begining to the end
        # dp = [0] * (n+3)
        # for i in range(3, n+3):
        #     dp[i] = min(dp[i-1]+1, dp[i-2]+4, dp[i-3]+9) + costs[i-3]
        # return dp[-1]
# @lc code=end

