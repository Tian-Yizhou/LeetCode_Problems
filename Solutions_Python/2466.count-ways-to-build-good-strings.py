'''
Author: Hannah
Date: 2026-01-23 22:20:28
LastEditTime: 2026-01-24 00:23:24
'''
#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#

# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        # Method 2
        MOD = 10**9 + 7
        dp = [1] + [0]*high

        for i in range(1, high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
            dp[i] = dp[i] % MOD
        
        return sum(dp[low:]) % MOD
        
        
        
        # Method 1
        # MOD = 10**9 + 7
        # @cache
        # def dp(i):
        #     if i < 0:
        #         return 0
        #     elif i == 0:
        #         return 1
        #     else:
        #         res = (dp(i-zero)+dp(i-one)) % MOD
        #         return res
        
        # return sum(dp(i) for i in range(low, high+1)) % MOD
# @lc code=end

