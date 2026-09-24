'''
Author: Hannah
Date: 2026-09-23 10:11:45
LastEditTime: 2026-09-23 10:27:33
'''
#
# @lc app=leetcode id=3634 lang=python3
#
# [3634] Minimum Removals to Balance Array
#

# @lc code=start
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Method: sliding window
        # Time complexity: O(n), n is the array length
        # Space complexity: O(1)
        # assume we have a valid array
        # consider a new element joins the array
        # if the array is not valid now, 
        # then we need to either remove its min element or max element
        # we can sort the array since it doesn't affect the result
        nums.sort()
        # enumerate max, delete min to make it valid
        max_remain = 0
        left = 0
        for right, num in enumerate(nums):
            # when the array is invalid, remove min element
            while nums[left] * k < num:
                left += 1
            # now the sub-array is valid, update the max remain elements
            max_remain = max(max_remain, right-left+1)

        # answer (delete times) is array length - element_remain
        return len(nums) - max_remain

# @lc code=end

