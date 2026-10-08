'''
Author: Hannah
Date: 2026-10-05 11:15:05
LastEditTime: 2026-10-07 20:03:29
'''
#
# @lc app=leetcode id=3592 lang=python3
#
# [3592] Inverse Coin Change
#

# @lc code=start
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        # Method: DP
        # time complexity: O(n^2)
        # space complexity: O(n)
        # dp[i]: the ways to get value i
        # if numWays[i] = dp[i], means all ways to get i are made by numbers less than i
        # if numWays[i] = dp[i] + 1, means we should have i as a number
        n = len(numWays)
        ans = []
        dp = [0] * (n+1)
        # corner case: there is one way to get value 0
        dp[0] = 1
        for i, way in enumerate(numWays, start=1):
            if way == dp[i]:
                continue
            if way != dp[i] + 1:
                return []
            ans.append(i)
            # the number i exist, use it to update the ways in dp
            for j in range(i, n+1):
                dp[j] += dp[j-i]

        return ans

# @lc code=end

