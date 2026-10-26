'''
Author: Hannah
Date: 2026-10-25 19:18:46
LastEditTime: 2026-10-25 19:55:39
'''
#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
import bisect
from math import inf
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # Method 1: Binary Search
        # time complexity: O(MlogM + NlogN + MlogN)
        # space complexity: O(1)
        # for each house, find its nearest heater, the max distance is answer
        n = len(heaters)
        houses.sort()
        heaters.sort()

        left_bound = 0
        ans = -inf
        for house in houses:

            idx = bisect.bisect_right(heaters, house, lo=left_bound)

            # calculate the distance to left heater and right heater
            left_dist = house - heaters[idx - 1] if idx > 0 else inf
            right_dist = heaters[idx] - house if idx < n else inf
            distance = min(left_dist, right_dist)

            ans = max(ans, distance)
            # move left bound: the house on the right, its position is at least idx
            left_bound = max(0, idx - 1)

        return ans
            


        
# @lc code=end

