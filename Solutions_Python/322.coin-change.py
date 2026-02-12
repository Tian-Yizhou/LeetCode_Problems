'''
Author: Hannah
Date: 2026-01-24 20:32:16
LastEditTime: 2026-01-24 20:59:46
'''
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Method 2
        # coin types
        c_t = len(coins)

        dp = [inf] * (amount+1)
        dp[0] = 0

        for i, coin in enumerate(coins):
            for j in range(1, amount+1):
                if j >= coin:
                    dp[j] = min(dp[j], dp[j-coin]+1)
        
        ans = dp[-1]

        return ans if ans < inf else -1



        # Method 1
        # coin types
        # c_t = len(coins)
        
        # dp = [[inf] * (amount+1) for _ in range(c_t+1)]
        # dp[0][0] = 0

        # for i, coin in enumerate(coins):
        #     for j in range(amount+1):
        #         if j < coin:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = min(dp[i][j], dp[i+1][j-coin] + 1)
        
        # ans = dp[c_t][amount]
        # return ans if ans < inf else -1
# @lc code=end

