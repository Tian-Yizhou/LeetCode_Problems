#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Method 2: DP, optimize method 1 space complexity
        # time complexity: O(N_s*N_t)
        # space complexity: O(N_t)
        n_s, n_t = len(s), len(t)
        dp = [1] + [0] * n_t
        for i, char_s in enumerate(s):
            for j in range(n_t-1, -1, -1):
                if char_s == t[j]:
                    dp[j+1] += dp[j]

        return dp[n_t]

        

        # Method 1: DP
        # time complexity: O(N_s*N_t)
        # space complexity: O(N_s*N_t)
        # dp[i][j]: the number of method to consist t[:j+1] using s[:i+1]
        n_s, n_t = len(s), len(t)
        dp = [[0] * (n_t + 1) for _ in range(n_s + 1)]
        for i in range(n_s+1):
            dp[i][0] = 1
        for i, char_s in enumerate(s):
            for j, char_t in enumerate(t):
                # if these two characters are different, we can only consist t[:j+1] using s[:i]
                dp[i+1][j+1] = dp[i][j+1]
                # if these two are the same, we can match them, meaning consist t[:j] using s[:i]
                if char_s == char_t:
                    dp[i + 1][j + 1] += dp[i][j]

        return dp[n_s][n_t]
# @lc code=end

