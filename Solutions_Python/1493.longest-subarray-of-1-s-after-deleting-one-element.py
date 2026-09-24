'''
Author: Hannah
Date: 2026-09-23 08:21:26
LastEditTime: 2026-09-23 10:09:50
'''
#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from collections import Counter
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Method: sliding window. A valid sub-array is an array contains at most one 0
        # Time complexity: O(n), n is the array length
        # Space complexity: O(1)
        ans = 0
        left = 0
        cnt0 = 0
        # check the valid right end
        for right, num in enumerate(nums):
            if num == 0:
                cnt0 += 1
            # if there is more than one 0 in the sub-array, move the left end
            while cnt0 > 1:
                if nums[left] == 0:
                    cnt0 -= 1
                left += 1
            # sub-array is valid now, update the answer
            # we need to delete the 0, so answer is NOT right-left+1
            ans = max(ans, right - left)

        return ans


# @lc code=end

