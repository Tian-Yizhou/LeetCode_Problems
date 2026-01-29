'''
Author: Hannah
Date: 2026-01-28 22:44:35
LastEditTime: 2026-01-29 00:00:06
'''
#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        # Method 4: iterative version of Method 3
        # dp0: doesn't hold stock on i-th day
        # dp1: hold stock on i-th day
        # dp2: doesn't hold stock on (i-2)th day
        dp0, dp1, dp2 = 0, -inf, 0

        for i in range(n):
            pre_0, pre_1, pre_2 = dp0, dp1, dp2
            dp2 = pre_0
            dp0 = max(pre_0, pre_1+prices[i])
            dp1 = max(pre_1, pre_2-prices[i])

        return dp0

        # Method 3
        # # s=0: we don't hold stock on i-th day; s=1: we hold stock on i-th day

        # @cache
        # def dfs(i, s):
        #     # impossible to hold stock at the beginning
        #     if i < 0:
        #         if s == 0:
        #             return 0
        #         else:
        #             return -inf
        #     # if we have stock today, there are 2 occasions
        #     if s == 1:
        #         # 1. we hold stock since yesterday
        #         # 2. we buy a stock today, and we didn't hold stock yesterday also didn't sell stock yesterday
        #         # meaning that we don't have stock (i-2)th day
        #         return max(dfs(i-1, 1), dfs(i-2, 0)-prices[i])
        #     # if we don't hold stock today
        #     else:
        #         # 1. we don't have a stock yesterday
        #         # 2. we sell a stock today(we have a stock yesterday)
        #         return max(dfs(i-1, 0), dfs(i-1, 1)+prices[i])

        # return dfs(n-1, 0)


        # Method 2
        # # s=0: hold stock; s=1: no stock, sold stock today; s=2: no stock, no sell 
        # @cache
        # def dfs(i, s):
        #     if i < 0:
        #         if s == 0:
        #             return -inf
        #         else:
        #          return 0
            
        #     # if we hold stock on i-th day, there are 2 occasions
        #     if s == 0:
        #         # 1. we hold it since yesterday
        #         # 2. buy it today, and yesterday is not cooldown
        #         return max(dfs(i-1, 0), dfs(i-1, 2) - prices[i])
        #     # if we sell the stock today
        #     elif s == 1:
        #         # we have stock yesterday
        #         return dfs(i-1, 0) + prices[i]
        #     # we have no stock today and we didn't sell it today
        #     else:
        #         # 1. we sold it yesterday, we are in cooldown
        #         # 2. we are not in cooldown, but we just don't buy stock today
        #         return max(dfs(i-1, 1), dfs(i-1, 2))

        # # the last day: we sell it today, or we sold it before
        # return max(dfs(n-1, 1), dfs(n-1, 2))

        # Method 1: add a status dimension
        # # dfs(i,s): the max profit on i-th day
        # # s==0: doesn't hold stock; s=1: hold stock
        # # cooldown==0: doesn't sell stock on i-th day; cooldown==1: sell stock on i-th day
        # # as long as s==1, cooldown must be 0
        # @cache
        # def dfs(i, s, cooldown):
        #     # we cannot hold stock at the beginning
        #     if i < 0:
        #         if s == 0:
        #             return 0
        #         else:
        #             return -inf
            
        #     # on i-th day
        #     # if we have stock, there are 2 occasions
        #     if s == 1:
        #         # 1. we hold stock on (i-1)th day
        #         # 2. we buy a stock and i-1 day satisfy cooldown=0
        #         return max(dfs(i-1, 1, 0), dfs(i-1, 0, 0)-prices[i])
        #     # if we don't have stock, there are 3 occasions
        #     else:
        #         # 1. we sold it (i-1)th day
        #         # 2. we didn't have stock on (i-1)th day and we didn't sell stock on (i-1)th day
        #         if cooldown == 0:
        #             return max(dfs(i-1, 0, 1), dfs(i-1, 0, 0))
        #         # 3. we sell stock today
        #         else:
        #             return dfs(i-1, 1, 0)+prices[i]
        
        # # the last day, you must not hold stock
        # # if you sold stock before, cooldown=0; if you sell stock on the last day, cooldown=1
        # ans = max(dfs(n-1, 0, 0), dfs(n-1, 0, 1))

        # return ans

# @lc code=end

