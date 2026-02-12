'''
Author: Hannah
Date: 2026-01-10 22:09:41
LastEditTime: 2026-01-10 22:24:56
'''
#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def lowerBound(self, nums, target): 
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def maximumCount(self, nums: List[int]) -> int:
       res = 0
       n = len(nums)

       num_neg = self.lowerBound(nums, 0)
       num_pos = n - self.lowerBound(nums, 1)

       return max(res, num_pos, num_neg)

# @lc code=end

