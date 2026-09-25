'''
Author: Hannah
Date: 2026-09-25 01:50:08
LastEditTime: 2026-09-25 02:48:45
'''
#
# @lc app=leetcode id=2321 lang=python3
#
# [2321] Maximum Score Of Spliced Array
#

# @lc code=start
from math import inf
class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:

        # Method 2: optimize time complexity
        # time complexity: O(n), but only loop array once
        # space complexity: O(1)
        sum1 = 0
        sum2 = 0
        
        # dp for nums1 and nums2
        dp1 = 0
        max_dp1 = 0
        dp2 = 0
        max_dp2 = 0
        
        for a, b in zip(nums1, nums2):
            # calculate sum
            sum1 += a
            sum2 += b
            
            # diff = nums1 - nums2
            diff = a - b 
            
            # if nums1 is source, -diff is the boost
            dp1 = max(dp1 - diff, 0)
            max_dp1 = max(max_dp1, dp1)
            # if nums2 is source, diff is the boost
            dp2 = max(dp2 + diff, 0)
            max_dp2 = max(max_dp2, dp2)
            
        return max(sum1 + max_dp1, sum2 + max_dp2)


        # Method 1: DP
        # time complexity: O(n), loop four times array
        # space complexity: O(1)
        # to raise the max score, we need to find the array with larger sum, call it numsLarge
        # then substitute a sub-array in it that is smaller than the same place sub-array in numsSmall
        # the larger the difference between these two sub-array is, the score raises more
        # this equals to find a sub-array that has max sum in numsLarge - numsSmall
        def MaxSumSubArray(nums_source, nums_target):
            dp = 0
            # the sub-array could be empty
            max_sum = 0
            for a, b in zip(nums_source, nums_target):
                # substitute the number in nums_source to nums_target
                diff = b-a
                # let num[i] join the sub-array ends with nums[i-1], or start a new sub-array
                dp = max(dp, 0) + diff
                max_sum = max(max_sum, dp)
                
            return max_sum

        sum1, sum2 = sum(nums1), sum(nums2)

        # use nums1 as source
        score1 = sum1 + MaxSumSubArray(nums1, nums2)
        # use nums2 as source
        score2 = sum2 + MaxSumSubArray(nums2, nums1)

        return max(score1, score2)

        

# @lc code=end

