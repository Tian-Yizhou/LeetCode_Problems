'''
Author: Hannah
Date: 2026-01-24 23:27:12
LastEditTime: 2026-01-25 00:16:26
'''
#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        # Method 2
        # dp[j]: the number of combinations that make up j using coins[:i+1]
        dp = [0] * (amount+1)
        dp[0] = 1

        for num in coins:
            for j in range(amount+1):
                if j >= num:
                    dp[j] = dp[j] + dp[j-num]
        
        return dp[amount]

        # Method 1
        # dp[i][j]: the number of combinations that make up j using coins[:i+1]
        # dp = [[0]*(amount+1) for _ in range(n+1)]
        # dp[0][0] = 1

        # for i, num in enumerate(coins):
        #     for j in range(amount+1):
        #         if j < num:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = dp[i][j] + dp[i+1][j-num]
        
        # return dp[n][amount]
# @lc code=end

