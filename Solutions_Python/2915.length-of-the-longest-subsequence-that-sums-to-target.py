'''
Author: Hannah
Date: 2026-01-24 21:01:59
LastEditTime: 2026-01-24 21:41:07
'''
#
# @lc app=leetcode id=2915 lang=python3
#
# [2915] Length of the Longest Subsequence That Sums to Target
#

# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        # Method 2
        # the j-th element of dp means the longest subsequence sums to j until current num in nums
        n = len(nums)
        dp = [-inf] * (target+1)
        dp[0] = 0

        for i, num in enumerate(nums):
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num]+1)
        
        ans = dp[target]

        return ans if ans > -inf else -1


        # Method 1
        # the (i, j) element of dp means the longest length of subsequence sums to j until i-th number in nums
        # n = len(nums)
        # dp = [[-inf] * (target+1) for _ in range(n+1)]
        # dp[0][0] = 0

        # for i, num in enumerate(nums):
        #     for j in range(target+1):
        #         if j < num:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = max(dp[i][j], dp[i][j-num]+1)
        
        # ans = dp[n][target]

        # return ans if ans > -inf else -1
# @lc code=end

