'''
Author: Hannah
Date: 2026-01-24 21:02:04
LastEditTime: 2026-01-24 23:10:39
'''
#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Method 3
        # the j-th element of dp means whether we can find a subsequence of nums[:i+1] sums to j
        n = len(nums)
        s = sum(nums)
        target = s // 2
        if s % 2 == 1:
            return False
        
        dp = [False] * (target+1)
        dp[0] = True

        for i, num in enumerate(nums):
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        
        return dp[target]

        # Method 2
        # the (i,j) element of dp means whether we can find a subsequence of nums[:i+1] sums to j
        # n = len(nums)
        # s = sum(nums)
        # target = s // 2
        # if s % 2 == 1:
        #     return False
        
        # dp = [[False] * (target+1) for _ in range(n+1)]
        # dp[0][0] = True

        # for i, num in enumerate(nums):
        #     for j in range(target+1):
        #         if j < num:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = dp[i][j] or dp[i][j-num]
        
        # return dp[n][target]


        # Method 1
        # the (i,j) element of dp means whether we can find a subsequence of nums[:i+1] sums to j
        # n = len(nums)
        # s = sum(nums)
        # target = s // 2
        # if s % 2 == 1:
        #     return False
        
        # @cache
        # def dp(i, j):
        #     # succeed before checking all the numbers
        #     if j == 0:
        #         return True
        #     # haven't succeed after checking all the numbers
        #     if i < 0 or j < 0:
        #         return False
            
        #     if j < nums[i]:
        #         return dp(i-1, j)
        #     else:
        #         return dp(i-1, j) or dp(i-1, j-nums[i])

        
        # return dp(n-1, target)
# @lc code=end

