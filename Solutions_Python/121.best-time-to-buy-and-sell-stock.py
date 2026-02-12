'''
Author: Hannah
Date: 2026-01-29 01:18:28
LastEditTime: 2026-02-02 23:37:18
'''
#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        min_price = inf
        ans = 0

        for i, price in enumerate(prices):
            ans = max(price - min_price, ans)

            if price < min_price:
                min_price = price
        
        return ans

# @lc code=end

