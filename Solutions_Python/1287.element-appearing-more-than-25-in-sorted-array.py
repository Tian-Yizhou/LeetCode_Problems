'''
Author: Hannah
Date: 2026-10-06 11:16:09
LastEditTime: 2026-10-06 11:56:37
'''
#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
# import bisect
class Solution:
    # find the smallest element > target
    def upper_bound(self, arr, target):
        n = len(arr)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            # if arr[mid] = target, continue search right
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def findSpecialInteger(self, arr: list[int]) -> int:

        # Method 2: binary search, 2 times
        # time complexity: O(logN)
        # space complexity: O(1)
        # we don't need to calculate the length of x, 
        # we just need to determine whether arr[j+m] equals arr[j]
        m = len(arr) // 4
        for i in (m, 2*m+1):
            x = arr[i]
            j = bisect.bisect_left(arr, x)
            if arr[j+m] == x:
                return x

        return arr[3*m + 2]

    
        # Method 1: binary search, 4 times
        # time complexity: O(logN)
        # space complexity: O(1)
        # maintain a window [left, right] for each unique element, 
        # then appearance time = right-left
        m = len(arr) // 4
        for i in (m, m*2 + 1):
            x = arr[i]
            if self.upper_bound(arr, x) - bisect.bisect_left(arr, x) > m:
                return x

        # if the answer is not arr[m] and arr[2m+1], it must be arr[3m+2]
        return arr[3*m + 2]

        
        
# @lc code=end

