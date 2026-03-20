'''
Author: Hannah
Date: 2026-02-01 11:29:14
LastEditTime: 2026-03-20 14:43:54
'''
#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Method 2: close interval
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]

        # Method 1: open interval
        left, right = -1, n-1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                # we can remove nums[right]
                right -= 1
            elif nums[mid] < nums[right]:
                # move right
                right = mid
            else:
                # move left
                left = mid
        
        return nums[right]
# @lc code=end

