'''
Author: Hannah
Date: 2026-01-24 01:14:11
LastEditTime: 2026-01-24 01:30:24
'''
#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # Method 2
        m, n = len(grid), len(grid[0])
        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return grid[0][0]
            return min(dp(i-1, j), dp(i, j-1)) + grid[i][j]
        
        return dp(m-1, n-1)





        # Method 1
        # m, n = len(grid), len(grid[0])
        # dp = [[0]*n]*m
        
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[0][0] = grid[0][0]
        #         elif i == 0 and j != 0:
        #             dp[i][j] = dp[i][j-1] + grid[i][j]
        #         elif i != 0 and j == 0:
        #             dp[i][j] = dp[i-1][j] + grid[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        # return dp[m-1][n-1]


# @lc code=end

