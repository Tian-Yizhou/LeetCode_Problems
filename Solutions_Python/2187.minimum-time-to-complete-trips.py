'''
Author: Hannah
Date: 2026-02-01 11:25:43
LastEditTime: 2026-02-14 13:49:31
'''
#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        n = len(time)
        # the range of time needed
        # totalTrips >= 1, then at least the fastest bus need to run once
        left = min(time) - 1
        # at most, the fatest bus need to run totoalTrips * t_min time
        right = totalTrips * min(time)

        # Method 2: open interval
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid
        
        return right

        # Method 1: close interval
        # the range of time needed
        # totalTrips >= 1, then at least the fastest bus need to run once
        left = min(time)
        # at most, the fatest bus need to run totoalTrips * t_min time
        right = totalTrips * left

        while left <= right:
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

# @lc code=end

