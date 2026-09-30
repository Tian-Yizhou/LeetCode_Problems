'''
Author: Hannah
Date: 2026-09-30 18:27:49
LastEditTime: 2026-09-30 18:35:07
'''
#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
# import bisect
class Solution:
    # find the largest index s.t. arr[idx] >= x
    def lower_bound(self, arr, x):
        n = len(arr)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            # if arr[mid] == x, continue search mid's left
            else:
                right = mid - 1
        return left
    
    def search(self, nums: list[int], target: int) -> int:

        # Method 2: bisect package
        ans = bisect.bisect_left(nums, target)
        if ans < len(nums) and nums[ans] == target:
            return ans
        else:
            return -1

        
        # Method 1: self-defined bisect_left
        # time complexity: O(logn)
        ans = self.lower_bound(nums, target)
        if ans < len(nums) and nums[ans] == target:
            return ans
        else:
            return -1
# @lc code=end

