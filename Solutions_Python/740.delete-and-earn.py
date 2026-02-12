'''
Author: Hannah
Date: 2026-01-23 21:27:39
LastEditTime: 2026-01-23 23:02:38
'''
#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:

        def rob(nums):
            f0, f1 = 0, 0
            for num in nums:
                f0, f1 = f1, max(f0+num, f1)
            return f1
        
        a = [0] * (max(nums) + 1)
        for num in nums:
            a[num] += num
        
        return rob(a)
# @lc code=end

