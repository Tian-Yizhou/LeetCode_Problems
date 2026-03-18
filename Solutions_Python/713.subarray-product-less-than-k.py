'''
Author: Hannah
Date: 2026-03-17 19:48:14
LastEditTime: 2026-03-17 20:05:50
'''
#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        prod = 1
        for right, x in enumerate(nums):
            prod *= x
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans

# @lc code=end

