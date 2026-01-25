'''
Author: Hannah
Date: 2026-01-24 21:02:09
LastEditTime: 2026-01-24 23:26:43
'''
#
# @lc app=leetcode id=2787 lang=python3
#
# [2787] Ways to Express an Integer as Sum of Powers
#

# @lc code=start
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        nums_p = [i**x for i in range(1, n+1)]

        # Method 2
        # dp[j] means the ways that we can find a subset of nums_p sums to j
        # dp = [0] * (n+1)
        # dp[0] = 1

        # for num in nums_p:
        #     for j in range(n, num-1, -1):
        #         if j >= num:
        #             dp[j] = dp[j] + dp[j-num]
        
        # return dp[n] % MOD

        # Method 1
        # dp[i][j] means the ways that we can find a subset of nums_p sums to j
        # dp = [[0] * (n+1) for _ in range(n+1)]
        # dp[0][0] = 1

        # for i, num in enumerate(nums_p):
        #     for j in range(n+1):
        #         if j < num:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = dp[i][j] + dp[i][j-num]
        
        # return dp[n][n] % MOD

        
# @lc code=end

