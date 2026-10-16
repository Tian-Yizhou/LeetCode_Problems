'''
Author: Hannah
Date: 2026-10-15 20:06:14
LastEditTime: 2026-10-15 20:38:10
'''
#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
from math import ceil
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        # Method: Binary Search
        # time complexity: O(NlogU), N=len(nums), U=max(nums)
        # space complexity: O(1)
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            # if mid is valid, move right end because we want to find the smallest valid mid
            if sum(ceil(x / mid) for x in nums) <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        return left
# @lc code=end

