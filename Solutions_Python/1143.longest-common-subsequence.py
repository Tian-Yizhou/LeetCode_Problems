'''
Author: Hannah
Date: 2026-01-25 12:25:40
LastEditTime: 2026-01-25 13:45:37
'''
#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1, n2 = len(text1), len(text2)

        # Method 2
        # dp[j]: the length of longest common subsequence of text[:i+1] and text[:j+1]
        dp = [0] * (n2+1)
        for i, s1 in enumerate(text1):
            pre = dp[0]
            for j, s2 in enumerate(text2):
                tmp = dp[j+1]
                if s1 == s2:
                    dp[j+1] = pre + 1
                else:
                    dp[j+1] = max(dp[j], dp[j+1])
                pre = tmp

        return dp[n2]

        # Method 1
        # dp[i][j]: the length of longest common subsequence of text[:i+1] and text[:j+1]
        # dp = [[0] * (n2+1) for _ in range(n1+1)]

        # for i, s1 in enumerate(text1):
        #     for j, s2 in enumerate(text2):
        #         if s1 == s2:
        #             dp[i+1][j+1] = dp[i][j] + 1
        #         else:
        #             dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        # return dp[n1][n2]
# @lc code=end

