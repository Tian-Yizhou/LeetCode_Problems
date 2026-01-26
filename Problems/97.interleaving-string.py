'''
Author: Hannah
Date: 2026-01-25 16:58:04
LastEditTime: 2026-01-25 19:51:51
'''
#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        # Method 2
        # dp[j]: whether we can use s1[:i], s2[:j] to consist s3[:i+j]
        dp = [False] * (n2+1)
        # if s1="", s2="", return True
        dp[0] = True

        # if s1="", s2 != "", dp[j] is True if s2[:j] == s3[:j]
        for j in range(n2):
            dp[j+1] = (dp[j] and (s2[j]==s3[j]))
        
        for i, c1 in enumerate(s1):
            # if s1 != 0, s2="", dp[0] is True if s1[:i] == s3[:i]
            dp[0] = (dp[0] and (c1 == s3[i]))
            for j, c2 in enumerate(s2):
                dp[j+1] = (c1 == s3[i+j+1] and dp[j+1]) or (c2 == s3[i+j+1] and dp[j])
            
        return dp[n2]

        # Method 1
        # # dp[i][j]: whether we can use s1[:i], s2[:j] to consist s3[:i+j]
        # dp = [[False] * (n2+1) for _ in range(n1+1)]
        # dp[0][0] = True

        # # if s1="", only return True if s2[:j]==s3[:j]
        # for j in range(n2):
        #     dp[0][j+1] = (s2[:j+1]==s3[:j+1])

        # for i, c1 in enumerate(s1):
        #     # if s2="", only return True if s1[:i]==s3[:i]
        #     dp[i+1][0] = (s1[:i+1]==s3[:i+1])
        #     for j, c2 in enumerate(s2):
        #         dp[i+1][j+1] = (c1 == s3[i+j+1] and dp[i][j+1]) or (c2 == s3[i+j+1] and dp[i+1][j])
        
        # return dp[n1][n2]


# @lc code=end

