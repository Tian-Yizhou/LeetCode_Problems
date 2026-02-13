'''
Author: Hannah
Date: 2026-02-01 11:29:52
LastEditTime: 2026-02-12 23:48:51
'''
#
# @lc app=leetcode id=1911 lang=python3
#
# [1911] Maximum Alternating Subsequence Sum
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        n = len(nums)

        # Method 2
        # same logic as method 1
        dp = [0, nums[0]]

        for i in range(1, n):
            pre_0 = dp[0]
            dp[0] = max(pre_0, dp[1]-nums[i])
            dp[1] = max(pre_0+nums[i], dp[1])

        return dp[1]

        # Method 1
        # # dfs(i, 0): the max alternating sum of a subsequence of nums[:i+1],
        # # which has even numbers
        # # dfs(i, 1): the max alternating sum of subsequence of nums[:i+1],
        # # which has odd numbers
        # @cache
        # def dfs(i, s):
        #     # boundary, we only have nums[0]
        #     if i == 0:
        #         # the subsequence max AS has odd numbers is [nums[0]]
        #         if s == 1:
        #             return nums[0]
        #         # the subsequence max AS has even numbers is []
        #         else:
        #             return 0
        #     # if we find the subsequence of nums[:i+1] that has odd numbers
        #     if s == 1:
        #         # either use the subsequence of nums[:i] with even numbers and choose nums[i]
        #         # or "inherit" a subsequence has odd elements that max AS from nums[:i-1]
        #         return max(dfs(i-1, 0)+nums[i], dfs(i-1, 1))
        #     # if we find the subsequence of nums[:i+1] that has even numbers
        #     else:
        #         # either use the subsequence of nums[:i] with odd numbers and choose nums[i]
        #         # or "inherit" a subsequence has even elements that max AS from nums[:i-1]
        #         return max(dfs(i-1, 1)-nums[i], dfs(i-1, 0))
        
        # return dfs(n-1, 1)

# @lc code=end

