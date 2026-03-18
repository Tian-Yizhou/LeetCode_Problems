'''
Author: Hannah
Date: 2026-03-17 19:50:35
LastEditTime: 2026-03-17 19:56:35
'''
#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        left = 0
        s = 0
        for right, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right-left+1)
                s -= nums[left]
                left += 1
        
        return ans if ans <= n else 0
# @lc code=end

