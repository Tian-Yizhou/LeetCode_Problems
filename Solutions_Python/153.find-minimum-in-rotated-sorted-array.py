'''
Author: Hannah
Date: 2026-02-01 11:33:37
LastEditTime: 2026-03-17 21:36:56
'''
#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:

    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Method 2: open interval (-1, n-1)
        left, right = -1, n-1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        
        return nums[right]

        # Method 1: close interval [0, n-2]
        # left, right = 0, n-2

        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] < nums[-1]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return nums[left]

# @lc code=end

