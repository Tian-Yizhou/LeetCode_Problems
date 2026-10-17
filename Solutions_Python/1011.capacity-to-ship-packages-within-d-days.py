'''
Author: Hannah
Date: 2026-10-17 11:20:50
LastEditTime: 2026-10-17 11:53:45
'''
#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def check(self, capacity, weights, days):
        # record the days needed to ship all packages
        need_days = 1
        current_weight = 0
        
        for weight in weights:
            # if this weight exceeds the capacity, we need a new day
            if current_weight + weight > capacity:
                need_days += 1
                # reset current weight
                current_weight = weight
            else:
                # add weight to current total weight
                current_weight += weight
                
        # return True if we can ship all packages
        return need_days <= days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # the min capacity: Max; the max capacity: sum
        # Method: Binary Search
        # time complexity: O(N + Nlog(\sum W - \max W))
        # space complexity: O(1)
        left, right = max(weights), sum(weights)
        # determine whether mid is able to do the task
        while left <= right:
            mid = (left + right) // 2
            # if packages can be shipped, move right end to continue searching left side
            if self.check(mid, weights, days):
                right = mid - 1
            else:
                left = mid + 1

        return left


# @lc code=end

