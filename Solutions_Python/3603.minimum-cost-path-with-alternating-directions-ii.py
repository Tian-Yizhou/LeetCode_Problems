'''
Author: Hannah
Date: 2026-09-25 04:20:15
LastEditTime: 2026-09-25 06:04:45
'''
#
# @lc app=leetcode id=3603 lang=python3
#
# [3603] Minimum Cost Path with Alternating Directions II
#

# @lc code=start
# from math import inf
# from functools import cache
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:

        # Method 3: DP, optimize method 1
        # time complexity: O(mn)
        # space complexity: O(n)
        dp = [inf] * (n + 1)
        # assume we enter from upside, note we cannot enter from leftside because we cannnot change dp[0]
        dp[1] = 0
        for i in range(m):
            for j in range(n):
                dp[j+1] = min(dp[j], dp[j+1]) + (i+1) * (j+1) + waitCost[i][j]

        return dp[n] - waitCost[0][0] - waitCost[m-1][n-1]



        # Method 2: DP
        # time complexity: O(mn)
        # space complexity: O(mn)
        # dp(i, j): the min cost to reach grid (i, j)
        @cache
        def dp(i, j):
            # the margin
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return 1

            return min(dp(i-1, j), dp(i, j-1)) + (i+1) * (j+1) + waitCost[i][j]

        return dp(m-1, n-1) - waitCost[m-1][n-1]

        
        # Method 1: DP
        # time complexity: O(mn)
        # space complexity: O(mn)
        # dp[i][j]: the min cost to reach grid (i, j)
        dp = [[inf] * (n+1) for _ in range(m+1)]
        # assume we start from the upside
        dp[0][1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                # note here since we expanded the margin of the grid, we need to adjust the value of i, j
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + i*j + waitCost[i-1][j-1]

        # no wait at the start and end
        return dp[m][n] - waitCost[0][0] - waitCost[m-1][n-1]


# @lc code=end

