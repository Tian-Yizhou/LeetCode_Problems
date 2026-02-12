#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Method 3: reverse
        tran_times = 2
        # dp[t][0]: the profit at the end of i-th day with no stock, t times transaction remain
        # dp[t][1]: the profit at the end of i-th day with stock, t times transaction remain
        # dp[0]: [-inf, inf] means you cannot have negative transaction times
        dp = [[-inf, -inf] for _ in range(tran_times+2)]
        # for t >= 0, s=0 then profit=0; s=1 is impossible
        for t in range(1, tran_times + 2):
            dp[t][0] = 0
        for p in prices:
            # reversely updating, t will not exceed tran_times, but might become nagative
            for t in range(tran_times + 1, 0, -1):
                dp[t][0] = max(dp[t][0], dp[t][1] + p)
                dp[t][1] = max(dp[t][1], dp[t-1][0] - p)
        
        return dp[-1][0]


        # Method 2: straight
        # tran_times = 2
        # # dp[t][0]: the profit at the end of i-th day with no stock, t times transaction remain
        # # dp[t][1]: the profit at the end of i-th day with stock, t times transaction remain
        # # initially, s=0 then profit=0; s=1 is impossible
        # dp = [[0, -inf] for _ in range(tran_times+1)]
        # # calculate the profit at the end of i-th day
        # for i in range(n):
        #     # each occassion
        #     for t in range(tran_times+1):
        #         # if you don't have stock, with t times transaction
        #         dp[t][0] = max(dp[t][0], dp[t][1]+prices[i])
        #         # if you have stock
        #         # no exceed transaction limit
        #         if t + 1 <= tran_times:
        #             dp[t][1] = max(dp[t][1], dp[t+1][0] - prices[i])
        #         # achieve transaction limit
        #         else:
        #             # it's impossible that you didn't trade but have a stock
        #             dp[t][1] = -inf
        
        # # the profit at the (n-1)th day under each occasion
        # profit = [max(dp[t]) for t in range(tran_times+1)]

        # return max(profit)

        # Method 1: Exceed Memory Limit
        # # dfs(i, s, tran): the max profit at the end of i-th day, with status s\
        # # remaining `t` transaction times
        # @cache
        # def dfs(i, s, t):
        #     # boundary
        #     if t > 2:
        #         return -inf
        #     if i < 0:
        #         if s == 0:
        #             return 0
        #         else:
        #             return -inf
            
        #     # trading
        #     if s == 1:
        #         return max(dfs(i-1, 1, t), dfs(i-1, 0, t+1)-prices[i])
        #     else:
        #         return max(dfs(i-1, 0, t), dfs(i-1, 1, t)+prices[i])
        
        # return max(dfs(n-1, 0, 0), dfs(n-1, 0, 1), dfs(n-1, 0, 2))


# @lc code=end

