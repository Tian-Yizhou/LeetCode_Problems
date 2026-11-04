'''
Author: Hannah
Date: 2026-11-03 19:17:03
LastEditTime: 2026-11-03 20:00:45
'''
#
# @lc app=leetcode id=960 lang=python3
#
# [960] Delete Columns to Make Sorted III
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # Method: DP
        # time complexity: O(n * len_s^2), n=len(strs), len_s=len(strs[0])
        # space complexity: O(len_s)
        len_s = len(strs[0])
        # dp[i]: the length of longest subsequence if strs end with i-th char
        dp = [0] * len_s
        # given i, iterate through all j < i, get the length of subsequence end with j-th char
        for i in range(len_s):
            for j in range(i):
                # if subsequence end with str[j] has larger length, and str[j] <= str[i]
                # we find a way to construct longer subsequence
                if dp[j] > dp[i] and all (s[j] <= s[i] for s in strs):
                    dp[i] = dp[j]
            # whatever connect to str[j] or not, str[i] add itself to the length
            dp[i] += 1

        return len_s - max(dp)
        
# @lc code=end

