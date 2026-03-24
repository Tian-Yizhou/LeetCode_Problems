'''
Author: Hannah
Date: 2026-02-01 11:31:31
LastEditTime: 2026-03-23 14:13:53
'''
#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start

# from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # Method: Dynamic Programming
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)

        # start from both ends, 
        # if two char are the same, we should keep both, result add 2
        # if two char are different, pick one that has longer subsequence length
        
        n = len(s)

        # Method 2
        dp = [[0]*n for _ in range(n)]
        # when updating dp[i][j], we need updated dp[i+1][j-1], dp[i+1][j], dp[i][j-1]
        # so we need to update reversely
        for i in range(n-1, -1, -1):
            # if sequence is empty, the value is 0 (initialization)
            # if only one character, length is 1
            dp[i][i] = 1
            # when there is a sequence
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) 
        
        return dp[0][n-1]

        # Method 1
        # dp(l, r): return the longest palindromic subsequence of s[l:r+1]
        @cache
        def dp(l, r):
            # if string is empty, return 0
            if l > r:
                return 0
            # if there is only one character, return 1
            if l == r:
                return 1
            # if l < r
            # if two characters are the same, keep both
            if s[l] == s[r]:
                return dp(l+1, r-1) + 2
            # Otherwise, keep the char with longer subsequence
            else:
                return max(dp(l+1, r), dp(l, r-1))
        
        return dp(0, n-1)

# @lc code=end

