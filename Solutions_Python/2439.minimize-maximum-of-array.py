'''
Author: Hannah
Date: 2026-02-01 11:26:05
LastEditTime: 2026-02-14 23:14:50
'''
#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        # Method 2: for each nums[i], i > 0, 
        # if nums[i] > avg(nums[:i]), then the avg(nums[:i+1]) is the min max bound
        # if nums[i] < avg(nums[:i]), then the min max bound is the avg(nums[:i])
        return max((s + i) // (i + 1) for i, s in enumerate(accumulate(nums)))


        # Method 1
        # given a limit, check whether all numbers in nums could <= limit
        def check(limit: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                # nums[i] take its own value and the part given by nums[i+1]
                new_num = nums[i] + extra
                extra = max(new_num - limit, 0)
            return nums[0] + extra <= limit

        # apply check to each element in range()
        # find the first true in range(nums[0], max(nums))
        # the range of minimum maximum integer is [nums[0], max(nums)]
        return bisect_left(range(max(nums)), True, lo=nums[0], key=check)

# @lc code=end

