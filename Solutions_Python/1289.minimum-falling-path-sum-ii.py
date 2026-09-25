'''
Author: Hannah
Date: 2026-09-25 11:09:18
LastEditTime: 2026-09-25 12:17:45
'''
#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#

# @lc code=start
# from math import inf
# from functools import cache
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        # Method 3: DP
        # time complexity: O(mn)
        # space complexity: O(1)
        # pre_min: the min value of last row
        # pre_min_col: the column index of last row min value
        # pre_second_min: the second min value of last row
        pre_min = 0
        pre_min_col = -1
        pre_second_min = 0

        for row in grid:
            # the min, second min of current row
            cur_min = inf
            cur_min_col = -1
            cur_second_min = inf

            for j, val in enumerate(row):
                # if current value is not in the same column with pre_min
                # we can add go the min value path
                if j != pre_min_col:
                    current_val = val + pre_min
                # if they are in the same column, use second min value
                else:
                    current_val = val + pre_second_min

                # update the min, second min sum of current row
                if current_val < cur_min:
                    cur_second_min = cur_min
                    cur_min = current_val
                    cur_min_col = j
                elif current_val < cur_second_min:
                    cur_second_min = current_val

            # update current row as previous row
            pre_min = cur_min
            pre_min_col = cur_min_col
            pre_second_min = cur_second_min

        return pre_min


        # Method 2: DP
        # dp(i, j): the min sum to achieve the bottom from grif=d[i][j]
        @cache
        def dp(i, j):
            if i == m - 1:
                return grid[i][j]

            min_sum = inf
            
            for k in range(n):
                if k != j:
                    min_sum = min(min_sum, dp(i + 1, k))
            
            return min_sum + grid[i][j]

        return min(dp(0, k) for k in range(n))



        # Method 1: DP
        # time complexity: O(mn^2)
        # space complexity: O(mn)
        # dp[i][j]: the min sum to achieve grid[i][j]
        dp = [[inf] * n for _ in range(m)]
        dp[0] = grid[0].copy()
        for i in range(1, m):
            for j in range(n):
                # choose which cell transfer to grid[i][j]
                for k in range(n):
                    if k != j:
                        dp[i][j] = min(dp[i][j], dp[i-1][k])
                dp[i][j] += grid[i][j]

        return min(dp[m-1])


# @lc code=end

