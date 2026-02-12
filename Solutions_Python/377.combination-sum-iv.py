'''
Author: Hannah
Date: 2026-01-23 22:20:38
LastEditTime: 2026-01-24 00:44:23
'''
#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # Method 2
        dp = [1] + [0]*target

        for i in range(1, target+1):
            dp[i] = sum([dp[i-num] for num in nums if num <= i])
        
        return dp[target]



        # Method 1
        # @cache
        # def dp(i):
        #     if i == 0:
        #         return 1
        #     else:
        #         return sum([dp(i-num) for num in nums if num <= i])
        # return dp(target)
        
# @lc code=end

