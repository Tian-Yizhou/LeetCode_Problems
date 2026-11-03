'''
Author: Hannah
Date: 2026-11-02 10:38:06
LastEditTime: 2026-11-02 12:35:36
'''
#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#

# @lc code=start
# from collections import Counter
class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        MOD = 1_000_000_007
        len_word = len(words[0])
        n = len(target)

        # Method 2: DP, optimize method 1 space complexity
        # space complexity: O(n)
        dp = [1] + [0] * n
        
        # count: for each index of word, how many times a char appeared at this position
        cnt = [Counter() for _ in range(len_word)]
        for word in words:
            for i in range(len_word):
                cnt[i][word[i]] += 1
        
        for k in range(len_word):
            for i in range(n-1, -1, -1):
                # 1. use k chars of words to form target[:i+1]
                # 2. use previous k-1 chars of words to form target[:i], then use the k-th char to form target[i]
                dp[i+1] = (dp[i+1] + cnt[k][target[i]] * dp[i]) % MOD

        return dp[n]

        # Method 1: DP
        # time complexity: O(len_word * n)
        # space complexity: O(len_word * n)
        # dp[i][j]: ways to form target[:i] using the first k characters of words[:j]
        # if there is no words, we have one way
        dp = [[1] + [0] * n for _ in range(len_word+1)]

        # count: for each index of word, how many times a char appeared at this position
        cnt = [Counter() for _ in range(len_word)]
        for word in words:
            for i in range(len_word):
                cnt[i][word[i]] += 1
        
        for k in range(len_word):
            for i in range(n):
                # 1. use k chars of words to form target[:i+1]
                # 2. use previous k-1 chars of words to form target[:i], then use the k-th char to form target[i]
                dp[k+1][i+1] = (dp[k][i+1] + cnt[k][target[i]] * dp[k][i]) % MOD

        return dp[len_word][n]
# @lc code=end

