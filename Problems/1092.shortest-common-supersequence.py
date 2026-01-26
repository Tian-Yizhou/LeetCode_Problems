'''
Author: Hannah
Date: 2026-01-25 16:58:16
LastEditTime: 2026-01-25 23:41:27
'''
#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n1, n2 = len(str1), len(str2)
        
        # Method 1
        # dp[i][j]: the length of shortest string that has both str1[:i] and str2[:j] as subsequences
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # if str1="", the length is the length of str2[:j]
        dp[0] = list(range(n2 + 1))
        for i in range(1, n1 + 1):
            # if str2="", the length is the length of str1[:i]
            dp[i][0] = i
        for i, s1 in enumerate(str1):
            for j, s2 in enumerate(str2):
                if s1 == s2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1

        ans = []
        i, j = n1 - 1, n2 - 1
        # from end to start, decide whether add the character to str3
        while i >= 0 and j >= 0:
            # if str1[i] == str2[j], str3 must have this character
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i -= 1
                j -= 1
            # if str1[i] != str2[j], and dp[i][j+1] is shorter, then it becomes dp[i+1][j+1] adding str1[i]
            elif dp[i+1][j + 1] == dp[i][j + 1]:
                ans.append(str1[i])
                i -= 1
            # if str1[i] != str2[j], and dp[i+1][j] is shorter, then it becomes dp[i+1][j+1] adding str2[j] 
            else:
                ans.append(str2[j])
                j -= 1

        return str1[:i + 1] + str2[:j + 1] + ''.join(reversed(ans))
        
# @lc code=end

