'''
Author: Hannah
Date: 2026-09-25 00:42:49
LastEditTime: 2026-09-25 01:49:49
'''
#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # Method: DP
        # time complexity: O(n)
        # space complexity: O(1)
        # if the max_sum sub-array is within the list, we can find the max sum sub-array
        # if the max_sum sub-array is cross the list, we can find the min sum sub-array
        
        dp_max = 0
        # the max_sum sub-array cannot be empty
        max_sum = -inf
        dp_min = 0
        # the min_sum sub-array could be empty
        min_sum = 0

        for num in nums:
            # either link current number to previous number, or start a new sub-array
            dp_max = max(dp_max, 0) + num
            max_sum = max(max_sum, dp_max)
            dp_min = min(dp_min, 0) + num
            min_sum = min(min_sum, dp_min)

        # if all numbers in nums are negative, then max_sum is the answer
        # in this case, sum(nums)-min_sum=0, is wrong answer
        if max_sum < 0:
            return max_sum
        # otherwise, the answer is choose the larger one
        else:
            return max(max_sum, sum(nums)-min_sum)
# @lc code=end

