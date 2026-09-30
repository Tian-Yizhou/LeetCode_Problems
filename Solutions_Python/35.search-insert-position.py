'''
Author: Hannah
Date: 2026-09-30 18:20:06
LastEditTime: 2026-09-30 18:24:23
'''
#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
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
            # when arr[mid]==x, continue search mid's left side
            else:
                right = mid - 1

        return left
    def searchInsert(self, nums: list[int], target: int) -> int:

        # Method 2: bisect package
        ans = bisect.bisect_left(nums, target)
        return ans
        
        # Method 1: self-defined bisect left
        # time complexity: O(logn)
        ans = self.lower_bound(nums, target)
        return ans

# @lc code=end

