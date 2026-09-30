#
# @lc app=leetcode id=3946 lang=python3
#
# [3946] Maximum Number of Items From Sale I
#

# @lc code=start
# from math import inf
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Method 1: DP
        # time complexity: O(n(n+budget)), n is len(items)
        # space complexity: O(budget)

        # stage 1: buy item i for the first time and get free copies
        # dp[j]: the max number of copies we can get for budget=j
        dp = [0] * (budget+1)
        # stage 2: buy an many cheapest item as possible
        min_price = inf

        # dp(i, b): the max number of copies, given items[:i+1] with budget b
        for factor, price in items:
            # update min_price
            min_price = min(min_price, price)
            # number of copies we can get if we buy item i
            cnt = 0
            for factor_j, _ in items:
                if factor_j % factor == 0:
                    cnt += 1

            # select or not select item i. If we buy it, at lease we need budget=price
            for j in range(budget, price-1, -1):
                dp[j] = max(dp[j], dp[j-price]+cnt)

        num_items = [dp_b + (budget-b) // min_price for b, dp_b in enumerate(dp)]

        return max(num_items)

# @lc code=end

