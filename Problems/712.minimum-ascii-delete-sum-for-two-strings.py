'''
Author: Hannah
Date: 2026-01-25 15:30:54
LastEditTime: 2026-01-25 16:28:55
'''
#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # get the string length and ASCII map
        n1, n2 = len(s1), len(s2)
        total = sum(map(ord, s1)) + sum(map(ord, s2))

        # Method 2
        # dp[j]: dp[i][j]: given s1[:i+1] and s2[:j+1], the maximun value of retained strings
        dp = [0] * (n2+1)

        for i, cha1 in enumerate(s1):
            pre = dp[0]
            for j, cha2 in enumerate(s2):
                tmp = dp[j+1]
                if cha1 == cha2:
                    dp[j+1] = pre + 2 * ord(cha1)
                else:
                    dp[j+1] = max(dp[j], dp[j+1])
                pre = tmp

        return total - dp[n2]

        # Method 1
        # dp[i][j]: given s1[:i+1] and s2[:j+1], the maximun value of retained strings
        # dp = [[0] * (n2+1) for _ in range(n1+1)]

        # for i, cha1 in enumerate(s1):
        #     for j, cha2 in enumerate(s2):
        #         if cha1 == cha2:
        #             dp[i+1][j+1] = dp[i][j] + 2 * ord(cha1)
        #         else:
        #             dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        # return total - dp[n1][n2]

# @lc code=end

