'''
Author: Hannah
Date: 2026-01-25 13:46:35
LastEditTime: 2026-01-25 15:04:35
'''
#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1, n2 = len(word1), len(word2)

        # Method 2
        # dp[i]: the minimum operations needed to convert word1[:i+1] to word2[:j+1]
        # if word1="", we need j+1 operations
        dp = list(range(n2+1))
        for i, s1 in enumerate(word1):
            pre = dp[0]
            # if word2="", we need i+1 operations
            dp[0] = i+1
            for j, s2 in enumerate(word2):
                tmp = dp[j+1]
                if s1 == s2:
                    dp[j+1] = pre
                else:
                    dp[j+1] = min(dp[j], dp[j+1], pre) + 1
                pre = tmp
        
        return dp[n2]

        # Method 1
        # dp[j][i]: the minimum operations needed to convert word1[:i+1] to word2[:j+1]
        # dp = [[inf] * (n1+1) for _ in range(n2+1)]
        # dp[0] = list(range(n1+1))

        # for j, s2 in enumerate(word2):
        #     dp[j+1][0] = j+1
        #     for i, s1 in enumerate(word1):
        #         if s1 == s2:
        #             dp[j+1][i+1] = dp[j][i]
        #         else:
        #             dp[j+1][i+1] = min(dp[j+1][i], dp[j][i+1], dp[j][i]) + 1
        
        # return dp[n2][n1]
# @lc code=end

