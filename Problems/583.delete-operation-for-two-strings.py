'''
Author: Hannah
Date: 2026-01-25 15:30:50
LastEditTime: 2026-01-25 16:55:03
'''
#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1, n2 = len(word1), len(word2)

        # Method 2
        # dp[j]: the minimum steps to make word1[:i+1] and word[:j+1] the same
        dp = list(range(n2+1))

        for i, s1 in enumerate(word1):
            pre = dp[0]
            dp[0] = i + 1
            for j, s2 in enumerate(word2):
                tmp = dp[j+1]
                if s1 == s2:
                    dp[j+1] = pre
                else:
                    dp[j+1] = min(dp[j], dp[j+1]) + 1
                pre = tmp
        
        return dp[n2]


        # Method 1
        # # dp[i][j]: the minimum steps to make word1[:i+1] and word[:j+1] the same
        # dp = [[inf] * (n2+1) for _ in range(n1+1)]
        # # if word1 = "", take j+1 steps to delete word2[:j+1]
        # dp[0] = list(range(n2+1))

        # for i, s1 in enumerate(word1):
        #     # if word2 = "", take i+1 steps to delete word1[:i+1]
        #     dp[i+1][0] = i + 1
        #     for j, s2 in enumerate(word2):
        #         # if s1 and s2 are the same character, no operation needed
        #         if s1 == s2:
        #             dp[i+1][j+1] = dp[i][j]
        #         # if s1 != s2, you can reach dp[i+1][j+1] by dp[i+1][j] or dp[i][j+1], and delete the s2 or s1
        #         else:
        #             dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
        
        # return dp[n1][n2]

# @lc code=end

