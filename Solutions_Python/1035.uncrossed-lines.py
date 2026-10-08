'''
Author: Hannah
Date: 2026-10-08 10:12:41
LastEditTime: 2026-10-08 10:58:32
'''
#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:

        # Method 2: DP, optimize method 1
        # space complexity: O(n2)
        n1, n2 = len(nums1), len(nums2)
        dp = [0] * (n2 + 1)
        for i, num1 in enumerate(nums1):
            # we need to record upper_left element, not using dp[j] because it will be replaced
            upper_left = 0
            for j, num2 in enumerate(nums2):
                # dp[j+1] itself will be the new upper_left for next state
                tmp = dp[j+1]
                if num1 == num2:
                    dp[j+1] = upper_left + 1
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                upper_left = tmp

        return dp[n2]

        # Method 1: DP
        # time complexity: O(n1*n2)
        # space complexity: O(n1*n2)
        # dp[i][j]: the max number of connecting lines given nums1[:i+1], nums2[:j+1]
        n1, n2 = len(nums1), len(nums2)
        # if there is no number in any arr, there is 0 line
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                # if two numbers are the same, we should always select them
                if num1 == num2:
                    dp[i+1][j+1] =dp[i][j] + 1
                # if the two numbers are different, we can select either one
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[n1][n2]

# @lc code=end

