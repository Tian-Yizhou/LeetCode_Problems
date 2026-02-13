'''
Author: Hannah
Date: 2026-02-01 11:24:15
LastEditTime: 2026-02-12 23:16:42
'''
#
# @lc app=leetcode id=2786 lang=python3
#
# [2786] Visit Array Positions to Maximize Score
#

# @lc code=start
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:

        n = len(nums)

        # Method 2
        # dp[0]: the max score of nums[:j+1] ending with even number
        # dp[1]: the max score of nums[:j+1] ending with odd number
        # boundary: we cannot start from nowhere
        dp = [-inf , -inf]
        # initialization: we must start from nums[0]
        if nums[0] % 2 == 1:
            dp[1] = nums[0]
        else:
            dp[0] = nums[0]

        for i in range(1, n):
            if nums[i] % 2 == 0:
                dp[0] = max(dp[0], dp[1]-x) + nums[i]
            else:
                dp[1] = max(dp[0]-x, dp[1]) + nums[i]
        
        return max(dp)
    
        # Method 1
        # @cache
        # def dfs(i, s):
        #     # end if i exceed nums length
        #     if i == len(nums):
        #         return 0
            
        #     # if nums[i]'s parity is the same as s, we must choose it
        #     # then for nums[i+1:], we either choose the same parity as s,
        #     # or choose the different parity and pay x
        #     if nums[i] % 2 == s:
        #         return max(dfs(i+1, s), dfs(i+1, s^1)-x) + nums[i]
        #     # if nums[i]'s parity is different from s, we skip it
        #     else:
        #         return dfs(i+1, s)
            
        # return dfs(0, nums[0]%2)
        
# @lc code=end

