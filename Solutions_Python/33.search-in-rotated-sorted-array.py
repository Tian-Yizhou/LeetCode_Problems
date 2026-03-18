'''
Author: Hannah
Date: 2026-02-01 11:35:12
LastEditTime: 2026-03-17 21:23:50
'''
#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:

    # a function to determine whether nums[idx] is
    # on the right hand side of target
    def is_rhs(self, idx, nums, target):
        end = nums[-1]
        # first, determine nums[idx] on the left slope or right slope;
        # then determine target on the left slope of right slope

        # if nums[idx] on the left slope
        if nums[idx] > end:
            # if target is on the left slope
            if target > end:
                return nums[idx] >= target
            # if target is on the right slope
            else:
                return False
        # if nums[idx] on the right slope
        else:
            # if target is on the left slope
            if target > end:
                return True
            # if target is on the right slope
            else:
                return nums[idx] >= target


    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # open interval: (-1, n)
        left , right = -1, n

        while left + 1 < right:
            mid  = (left + right) // 2
            # if nums[mid] is on the right side of target, or include target
            if self.is_rhs(mid, nums, target):
                right = mid
            else:
                left = mid
        
        if right < n and nums[right] == target:
            return right
        else:
            return -1


# @lc code=end

