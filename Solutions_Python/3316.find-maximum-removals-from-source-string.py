#
# @lc app=leetcode id=3316 lang=python3
#
# [3316] Find Maximum Removals From Source String
#

# @lc code=start
# from math import inf
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        # for a given idx in targetIndices, we consider
        # if we remove it, is source still valid? if valid, ans+1
        # if we don't remove it, the ans stays the same as without it
        
        n = len(source)
        m = len(pattern)
        targetIndices = set(targetIndices)

        # Method 2: DP, optimize Method 1 space complexity
        # space complexity: O(m)
        dp = [-inf] * (m+1)
        dp[0] = 0

        for i in range(n):
            can_del = 1 if i in targetIndices else 0

            for j in range(min(i, m-1), -1, -1):
                res = dp[j + 1] + can_del
                if source[i] == pattern[j]:
                    res = max(res, dp[j])
                dp[j + 1] = res

            dp[0] += can_del

        return dp[m]


        # Method 1: DP
        # time complexity: O(nm)
        # space complexity: O(nm)
        # dp[i][j]: the max ops to keep pattern[:j] is a subsequence of source[:i]
        dp = [[-inf] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(n):
            can_del = 1 if i in targetIndices else 0
            # when there is no char in pattern, and i is in targetIndices, 
            # we can delete char to add one operation count
            dp[i + 1][0] = dp[i][0] + can_del
            # pattern[:j] must have at least i chars
            for j in range(min(i + 1, m)):
                # if we don't match source[i] with pattern[j]
                # we can delete source[i] to add 1 ops count if i is in targetIndices
                res = dp[i][j + 1] + can_del
                # if we match source[i] with pattern[j], we don't delete source[i]
                # then the situation is the same as we don't have sourse[i] and pattern[j]
                if source[i] == pattern[j]:
                    res = max(res, dp[i][j])
                dp[i + 1][j + 1] = res

        return dp[n][m]

# @lc code=end

