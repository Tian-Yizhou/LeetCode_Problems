'''
Author: Hannah
Date: 2026-01-24 23:27:17
LastEditTime: 2026-01-24 23:55:06
'''
#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:

        # First, we need to construct the perfect square sequence
        max_num = int(n**(0.5)) + 1
        nums = [i**2 for i in range(1, max_num+1)]

        # Method 2
        # dp[j] means the least number of numbers in nums[:i+1] that sums to j
        dp = [inf] * (n+1)
        dp[0] = 0

        for num in nums:
            for j in range(n+1):
                if j >= num:
                    dp[j] = min(dp[j], dp[j-num]+1)
        
        return dp[n]
        
        # Method 1
        # dp[i][j] means the least number of numbers in nums[:i+1] that sums to j
        # dp = [[inf] * (n+1) for _ in range(max_num+1)]
        # dp[0][0] = 0

        # for i, num in enumerate(nums):
        #     for j in range(n+1):
        #         if j < num:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = min(dp[i][j], dp[i+1][j-num]+1)
        

        # return dp[max_num][n]



# @lc code=end

