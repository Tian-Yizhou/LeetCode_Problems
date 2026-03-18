'''
Author: Hannah
Date: 2026-02-01 11:33:27
LastEditTime: 2026-03-17 21:45:51
'''
#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # open interval
        left, right = -1, n-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid
        
        return right
# @lc code=end

