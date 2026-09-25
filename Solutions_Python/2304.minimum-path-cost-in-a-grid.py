'''
Author: Hannah
Date: 2026-09-25 06:06:00
LastEditTime: 2026-09-25 11:08:48
'''
#
# @lc app=leetcode id=2304 lang=python3
#
# [2304] Minimum Path Cost in a Grid
#

# @lc code=start
class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Method 2: DP
        # time complexity: O(mn^2)
        # space complexity: O(n)
        dp = grid[0].copy()
        for i in range(1, m):
            cur_dp = [0] * n
            for j, val in enumerate(grid[i]):
                cur_dp[j] = min(
                    dp[idx] + moveCost[pre_val][j] for idx, pre_val in enumerate(grid[i-1])
                    ) + val
            dp = cur_dp

        return min(dp)

        # Method 1: DP
        # time complexity: O(mn^2)
        # space complexity: O(mn)
        # dp[i][j]: the min cost path to achieve grid[i][j]
        dp = [[0]*n for _ in range(m)]
        dp[0] = grid[0]
        for i in range(1, m):
            for j, val in enumerate(grid[i]):
                dp[i][j] = min(
                    dp[i-1][idx] + moveCost[pre_val][j] for idx, pre_val in enumerate(grid[i-1])
                    ) + val

        return min(dp[m-1])
# @lc code=end

