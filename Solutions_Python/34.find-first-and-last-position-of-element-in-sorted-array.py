'''
Author: Hannah
Date: 2026-09-30 17:46:22
LastEditTime: 2026-09-30 18:18:07
'''
#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# import bisect
class Solution:
    # find the first index s.t. arr[idx] >= x
    def my_bisect_left(self, arr, x):
        n = len(arr)
        # [left, right] interval is undetermined
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left
    # find the first index s.t. arr[idx] > x
    def my_bisect_right(self, arr, x):
            n = len(arr)
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                # when arr[mid] == x, continue search mid's right side
                if arr[mid] <= x:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # Method 2: bisect package
        lower_bound = bisect.bisect_left(nums, target)
        upper_bound = bisect.bisect_right(nums, target)
        if lower_bound == upper_bound:
            return [-1, -1]
        else:
            return [lower_bound, upper_bound - 1]
        
        # Method 1: bisect
        # self-defined bisect_left and bisect_right function
        lower_bound = self.my_bisect_left(nums, target)
        upper_bound = self.my_bisect_right(nums, target)
        if lower_bound == upper_bound:
            return [-1, -1]
        else:
            return [lower_bound, upper_bound - 1]
# @lc code=end

