'''
Author: Hannah
Date: 2026-02-01 11:25:28
LastEditTime: 2026-02-14 12:23:47
'''
#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        ans = 0
        nums.sort()

        # for each number
        for i in range(n):
            
            # select searching range: nums[i+1:]
            idx_start = bisect_left(nums, lower-nums[i], lo=i+1)
            idx_end = bisect_right(nums, upper-nums[i], lo=i+1)

            ans += idx_end - idx_start

        return ans
# @lc code=end

