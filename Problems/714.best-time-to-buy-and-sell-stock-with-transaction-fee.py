'''
Author: Hannah
Date: 2026-02-01 11:23:56
LastEditTime: 2026-02-03 00:47:47
'''
#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)

        # Method 2
        # dp[0]: the max profit at the end of i-th day without stock
        # dp[1]: the max profit at the end of i-th day with stock
        dp = [0, -inf]
        for i in range(n):
            pre_0 = dp[0]
            dp[0] = max(pre_0, dp[1]+prices[i])
            dp[1] = max(dp[1], pre_0-prices[i]-fee)
        
        return dp[0]

        # Method 1
        # # dfs(i, s): the max profit at the end of i-th day, where s==1 stands for hold stock
        # @cache
        # def dfs(i,s):
        #     if i < 0:
        #         if s == 1:
        #             return -inf
        #         else:
        #             return 0
            
        #     if s == 1:
        #         return max(dfs(i-1, 1), dfs(i-1, 0)-prices[i]-fee)
        #     else:
        #         return max(dfs(i-1, 0), dfs(i-1, 1)+prices[i])
        
        # return dfs(n-1, 0)
# @lc code=end

