'''
Author: Hannah
Date: 2026-01-25 16:58:09
LastEditTime: 2026-01-25 21:09:23
'''
#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#

# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        n1, n2 = len(nums1), len(nums2)

        # Method 2
        # dp[j]: the max dot product of subsequence from nums1[:], nums[:j]
        dp = [-inf] * (n2+1)

        for i, num1 in enumerate(nums1):
            pre = dp[0]
            for j, num2 in enumerate(nums2):
                tmp = dp[j+1]
                dp[j+1] = max(
                    max(pre, 0) + num1*num2, dp[j], dp[j+1]
                    )
                pre = tmp
        
        return dp[n2]

        # # Mehod 1
        # # dp[i][j]: the max dot product of subsequence from nums1[:i], nums2[:j]
        # dp = [[-inf] * (n2+1) for _ in range(n1+1)]
        
        # for i, num1 in enumerate(nums1):
        #     for j, num2 in enumerate(nums2):
        #         dp[i+1][j+1] = max(
        #             max(dp[i][j], 0)+num1*num2, dp[i+1][j], dp[i][j+1]
        #          )
        
        # return dp[n1][n2]

# @lc code=end

