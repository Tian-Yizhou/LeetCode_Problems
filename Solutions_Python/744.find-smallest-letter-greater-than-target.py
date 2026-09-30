'''
Author: Hannah
Date: 2026-09-30 18:35:21
LastEditTime: 2026-09-30 18:41:21
'''
#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
# import bisect
class Solution:
    # find the largest index s.t. arr[idx] > x
    def upper_bound(self, arr, x):
        n = len(arr)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            # if arr[mid] == x, continue search mid's right side
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)

        # Method 2: bisect_right package
        idx = bisect.bisect_right(letters, target)
        if idx == n:
            return letters[0]
        else:
            return letters[idx]

        
        # Method 1: self-defined bisect_right
        # time complexity: O(logn)
        idx = self.upper_bound(letters, target)
        if idx == n:
            return letters[0]
        else:
            return letters[idx]

# @lc code=end

