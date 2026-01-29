#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        # Method 2
        # dp[0]: the profit on i-th day without stock; dp[1]: the profit on i-th day with stock
        dp = [0, -inf]
        for i in range(n):
            pre_0, pre_1 = dp[0], dp[1]
            dp[0] = max(pre_0, pre_1 + prices[i])
            dp[1] = max(pre_0 - prices[i], pre_1)
        
        return dp[0]
        
        # Method 1
        # # dfs(i, s): the profit at the end of i-th day
        # # s==0: we don't have stock; s==1: we have stock
        # @cache
        # def dfs(i, s):
        #     if i < 0:
        #         if s == 1:
        #             return -inf
        #         else:
        #             return 0
            
        #     if s == 1:
        #         return max(dfs(i-1, 1), dfs(i-1, 0) - prices[i])
        #     else:
        #         return max(dfs(i-1, 0), dfs(i-1, 1) + prices[i])
        
        # ans = dfs(n-1, 0)

        # return ans
# @lc code=end

