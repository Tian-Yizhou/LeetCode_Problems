'''
Author: Hannah
Date: 2026-11-02 10:39:20
LastEditTime: 2026-11-02 20:10:37
'''
#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
# import bisect
# from math import inf
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        # Method 2: Greedy
        # time complexity: O(N), N=len(nums)
        # space complexity: O(1)
        # maintain the smallest num and second smallest num,
        # if we can find any number > second smallest num, then we find the answer
        first, second = inf, inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


        
        # Method 1: Longest Increasing Sequence
        # time complexity: O(NlogK), N=len(nums), K=len(increasing_sequence)
        # space complexity: O(K)
        # find the longest increasing sequence of nums, if its length
        # is larger than 3, then we can find i, j, k we want
        increasing_sequence = []
        for num in nums:
            idx = bisect.bisect_left(increasing_sequence, num)
            # if increasing_sequence has 3 numbers, we find the answer
            if idx == 2:
                return True
            # if num is the largest, add it to increasing_sequence
            if idx == len(increasing_sequence):
                increasing_sequence.append(num)
            # if num >= increasing_sequence[idx-1] and num < increasing_sequence[idx], 
            # substitute increasing_sequence[i] with num
            else:
                increasing_sequence[idx] = num

        return False
# @lc code=end

