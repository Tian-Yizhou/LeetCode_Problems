'''
Author: Hannah
Date: 2026-10-08 10:59:26
LastEditTime: 2026-10-08 11:59:47
'''
#
# @lc app=leetcode id=3290 lang=python3
#
# [3290] Maximum Multiplication Score
#

# @lc code=start
# from functools import cache
# from math import inf
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)

        # Method 3: DP, optimize method 1
        # space complexity: O(4)
        dp = [-inf] * 5
        dp[0] = 0
        for i, x in enumerate(b):
            # we need to record upper_left because dp[j] will be updated
            upper_left = 0
            for j, y in enumerate(a):
                tmp = dp[j+1]
                dp[j+1] = max(upper_left + x*y, dp[j+1])
                upper_left = tmp

        return dp[4]

        # Method 2: DP
        # time complexity: O(4N), N=len(b)
        # space complexity: O(4N)
        # dp[i][j]: same as method 1
        dp = [[0] * 5 for _ in range(n+1)]
        dp[0][1:] = [-inf] * 4
        for i in range(n):
            for j in range(4):
                dp[i+1][j+1] = max(dp[i][j] + b[i]*a[j], dp[i][j+1])

        return dp[n][4]


        # Method 1: DP
        # time complexity: O(4N), N=len(b)
        # space complexity: O(4N)
        # dp(i, j): the max value we can get, if we choose j+1 numbers in b[:i+1]
        # and let them multiply with a[0] to a[j]
        @cache
        def dp(i, j):
            # boundary case
            # if there is no number in a, we have finished
            # we cannot add value to result, return 0
            if j < 0:
                return 0
            # if there is no number in b, but still number in a
            # it's invalid, return -inf
            if i < 0:
                return -inf
            # if we let b[i] multiply with a[j], we have dp[i-1][j-1] + b[i]*a[j]
            # if we don't let b[i] multiply with a[j], we have dp[i-1][j]
            return max(dp(i-1, j-1) + b[i]*a[j], dp(i-1, j))

        ans = dp(n-1, 3)
        dp.cache_clear()

        return ans
# @lc code=end

