'''
Author: Hannah
Date: 2026-01-26 10:21:20
LastEditTime: 2026-02-03 00:58:10
'''
#
# @lc app=leetcode id=2826 lang=python3
#
# [2826] Sorting Three Groups
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        n = len(nums)

        # Method 2
        # dp[x]: the length of longest non-decreasing subsequence ends with number x
        dp = [0] * 4
        for num in nums:
            # for the current number, all the subsequence ends with x, where x <= num, 
            # the length could add 1
            dp[num] = max(dp[1:num+1]) + 1
        
        return n - max(dp)


        # Method 1
        # # equivalently, we can try to find the longest non-decreasing subsequence
        # # dp[i]: the length of longest non-decreasing subsequence of nums[:i]
        # dp = [0] * n

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] >= nums[j]:
        #             dp[i] = max(dp[j], dp[i])
            
        #     dp[i] += 1
        
        # return n - max(dp)
        # @lc code=end

