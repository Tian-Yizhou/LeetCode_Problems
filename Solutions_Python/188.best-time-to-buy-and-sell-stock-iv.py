'''
Author: Hannah
Date: 2026-01-29 00:07:02
LastEditTime: 2026-01-29 01:17:20
'''
#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)

        # Method 3: iterative version of Method 2
        dp = [[-inf, -inf] for _ in range(k+2)]
        for j in range(1, k+2):
            dp[j][0] = 0
        
        for i in range(n):
            for j in range(k+1, 0, -1):
                pre_0, pre_1 = dp[j][0], dp[j][1]
                # if we don't have stock
                dp[j][0] = max(dp[j][0], dp[j][1]+prices[i])
                # if we have stock
                dp[j][1] = max(dp[j][1], dp[j-1][0]-prices[i])
        
        return dp[k+1][0]
        

        # Method 2
        # dfs(i, s, j): the max profit at the end of i-th day with at most j times transactions
        @cache
        def dfs(i, s, j):
            # we need to justify the transaction times first
            if j < 0:
                return -inf
            
            if i < 0:
                if s == 0:
                    return 0
                else:
                    return -inf
            
            # if we have stock today
            if s == 1:
                # 1. we have stock since yesterday
                # 2. we buy stock today (1 more transaction than yesterday)
                return max(dfs(i-1, 1, j), dfs(i-1, 0, j-1)-prices[i])
            # if we don't have stock today
            else:
                # 1. we don't have stock since yesterday
                # 2. we sell it today (doesn't cost transaction times)
                return max(dfs(i-1, 0 ,j), dfs(i-1, 1, j)+prices[i])
        
        return dfs(n-1, 0, k)

        # Method 1
        # dfs(i, s, j): the max profit at the end of i-th day remaining j times transactions
        # s=0: we don't have stock; s=1: we have stock
        # Note: If we buy a stock, we will definitely sell it
        @cache
        def dfs(i, s, j):
            if i < 0:
                if s == 0:
                    return 0
                else:
                    return -inf
            
            # if we don't have stock on i-th day
            if s == 0:
                # if we can trade
                if j > 0:
                    # 1. we don't have a stock yesterday and don't buy a stock today
                    # 2. we sell a stock today (we have a stock yesterday), this doesn't add transaction times
                    return max(dfs(i-1, 0, j), dfs(i-1, 1, j)+prices[i])
                # if we cannot trade
                else:
                    # we can just keep the profit of yesterday (to max profit, we will not keep stock)
                    return dfs(i-1, 0, j)
            # if we have stock on i-th day
            else:
                # if we can trade
                if j > 0:
                    # 1. we buy a stock today (we don't have stock yesterday)
                    # 2. we keep the stock since yester day
                    return max(dfs(i-1, 0, j-1)-prices[i], dfs(i-1, 1, j))
                # if we cannot trade
                else:
                    # we keep the stock since yesterday
                    return dfs(i-1, 1, j)
        
        return dfs(n-1, 0, k)
# @lc code=end

