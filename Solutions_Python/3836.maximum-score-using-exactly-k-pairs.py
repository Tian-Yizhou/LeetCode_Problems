#
# @lc app=leetcode id=3836 lang=python3
#
# [3836] Maximum Score Using Exactly K Pairs
#

# @lc code=start
# from math import inf
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        n, m = len(nums1), len(nums2)

        # Method 2: DP, optimize the space complexity of Method 1
        # space complexity: O(mn)        
        f = [[0] * (m + 1) for _ in range(n + 1)]
        g = [[0] * (m + 1) for _ in range(n + 1)]
        invalid = [-inf] * (m - k + 1)
        for l in range(1, k + 1):
            g[l - 1][l: -(k - l)] = invalid
            for i in range(l - 1, n - (k - l)):  # 后面还要选 K-k 个下标对
                g[i + 1][l - 1] = -inf
                for j in range(l - 1, m - (k - l)):
                    g[i + 1][j + 1] = max(g[i][j + 1], g[i + 1][j], f[i][j] + nums1[i] * nums2[j])
            f, g = g, f
        return f[n][m]

        # Method 1: DP
        # time complexity: O(kmn)
        # space complexity: O(kmn)
        # dp[k][i][j]: the max score we can earn using nums1[:i+1] and nums2[:j+1] consisting k pairs
        dp = [[[-inf] * (m + 1) for _ in range(n + 1)] for _ in range(k + 1)]
        dp[0] = [[0] * (m + 1) for _ in range(n + 1)]
        for l in range(1, k+1):
            for i in range(l-1, n-(k-l)):
                for j in range(l-1, m-(k-l)):
                    # if nums2[j] is not chosen, the max score stays the same as without it
                    # if nums2[j] is chosen, it can pair with nums1[i] or nums[i-1]
                    dp[l][i+1][j+1] = max(dp[l][i+1][j], dp[l][i][j+1], dp[l-1][i][j] + nums1[i] * nums2[j])

        return dp[k][n][m]
# @lc code=end

