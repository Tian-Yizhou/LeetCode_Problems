'''
Author: Hannah
Date: 2026-09-26 07:12:22
LastEditTime: 2026-09-26 08:17:27
'''
#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#

# @lc code=start
# from functools import cache
# from math import inf
class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:

        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])

        # to get the max non-negative product path to grid[i][j], 
        # we need to know the max prod path and min prod path 
        # to grid[i-1][j] and grid[i][j-1]
        # because the max_prod_path comes from either max_prod or min_prod due to sign flip
        
        # Method 3: DP, optimize method 2
        # time complexity: O(mn)
        # space complexity: O(n)
        dp = [None] * n
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i == 0 and j == 0:
                    dp[0] = (val, val)
                    continue

                min_prod, max_prod = inf, -inf
                if i > 0:
                    min_prod_up, max_prod_up = dp[j]
                    min_prod = min(min_prod_up * val, max_prod_up * val)
                    max_prod = max(min_prod_up * val, max_prod_up * val)
                if j > 0:
                    min_prod_left, max_prod_left = dp[j-1]
                    min_prod = min(min_prod, min_prod_left * val, max_prod_left * val)
                    max_prod = max(max_prod, min_prod_left * val, max_prod_left * val)
                dp[j] = (min_prod, max_prod)

        ans = dp[n-1][1]
        return ans % MOD if ans >= 0 else -1



        # Method 2: DP
        # time complexity: O(mn)
        # space complexity: O(mn)
        # dp[i][j]: the min_prod and max_prod to achieve grid[i][j]
        dp = [[None] * n for _ in range(m)]

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i == 0 and j == 0:
                    dp[0][0] = (val, val)
                    continue

                min_prod, max_prod = inf, -inf
                if i > 0:
                    min_prod_up, max_prod_up = dp[i-1][j]
                    min_prod = min(min_prod_up * val, max_prod_up * val)
                    max_prod = max(min_prod_up * val, max_prod_up * val)
                if j > 0:
                    min_prod_left, max_prod_left = dp[i][j-1]
                    min_prod = min(min_prod, min_prod_left * val, max_prod_left * val)
                    max_prod = max(max_prod, min_prod_left * val, max_prod_left * val)
                dp[i][j] = (min_prod, max_prod)
        
        ans = dp[m-1][n-1][1]
        return ans % MOD if ans >= 0 else -1

        # Method 1: DP
        # time complexity: O(mn)
        # space complexity: O(mn)
        # dp(i, j): the min_prod and max_prod to achieve grid[i][j]
        @cache
        def dp(i, j):
            val = grid[i][j]
            if i == 0 and j == 0:
                return val, val
            # calculate the min_prod and max_prod from upside and leftside
            min_prod, max_prod = inf, -inf
            if i > 0:
                min_prod_up, max_prod_up = dp(i-1, j)
                min_prod = min(min_prod_up * val, max_prod_up * val)
                max_prod = max(min_prod_up * val, max_prod_up * val)
            if j > 0:
                min_prod_left, max_prod_left = dp(i, j-1)
                min_prod = min(min_prod, min_prod_left * val, max_prod_left * val)
                max_prod = max(max_prod, min_prod_left * val, max_prod_left * val)

            return min_prod, max_prod

        ans = dp(m-1, n-1)[1]
        return ans % MOD if ans >= 0 else -1

# @lc code=end

