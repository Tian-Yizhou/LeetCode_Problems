'''
Author: Hannah
Date: 2026-01-23 21:27:31
LastEditTime: 2026-01-23 22:19:29
'''
#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        def solve(sub_nums):
            f0, f1 = 0, 0
            for num in sub_nums:
                f0, f1 = f1, max(f0+num, f1)
            return f1
        
        return max(solve(nums[1:]), nums[0]+solve(nums[2:-1]))


        # from beginning to the end
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp_1 = [0] * (n+1)
        # dp_2 = [0] * (n+1)
        # for i in range(2, n+1):
        #     dp_1[i] = max(dp_1[i-1], dp_1[i-2]+nums[i-2])
        #     dp_2[i] = max(dp_2[i-1], dp_2[i-2]+nums[i-1])
        
        # return max(dp_1[-1], dp_2[-1])
# @lc code=end

