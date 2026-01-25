'''
Author: Hannah
Date: 2026-01-24 10:52:16
LastEditTime: 2026-01-24 20:25:33
'''
#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Method 2
        s = sum(nums) - abs(target)
        if s<0 or s%2 == 1:
            return 0
        bag_size = s // 2
        n = len(nums)

        dp = [0] * (bag_size+1)
        dp[0] = 1

        for num in nums:
            for j in range(bag_size, num-1, -1):
                dp[j] = dp[j] + dp[j-num]
        
        return dp[-1]

        # Method 1
        # s = sum(nums)-abs(target)
        # if s<0 or s%2 == 1:
        #     return 0
        # bag_size = s // 2
        # n = len(nums)

        # dp = [[0] * (bag_size+1) for _ in range(n+1)]
        # dp[0][0] = 1

        # for i, num in enumerate(nums):
        #     for j in range(bag_size+1):
        #         if j < num:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = dp[i][j] + dp[i][j-num]
        
        # return dp[n][bag_size]


# @lc code=end

