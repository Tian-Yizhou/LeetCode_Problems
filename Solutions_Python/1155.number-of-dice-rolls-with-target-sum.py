'''
Author: Hannah
Date: 2026-10-07 20:05:37
LastEditTime: 2026-10-07 22:39:57
'''
#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        # if target is not within the range, it's impossible
        if not (n <= target <= n*k):
                    return 0

        # Method: DP
        # time complexity: O(n*k*(target-n+1))
        # space complexity: O(n*(target-n+1))
        # dp[i][j]: use i dices to get value j
        dp = [[0] * (target - n + 1) for _ in range(n+1)]
        # if there is no dice, value is 0, there is one method
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(target - n + 1):
                for x in range(min(k, j+1)):
                      dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % MOD

        return dp[n][target-n]


# @lc code=end

