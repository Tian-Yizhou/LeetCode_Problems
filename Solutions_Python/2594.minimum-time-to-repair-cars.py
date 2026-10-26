'''
Author: Hannah
Date: 2026-10-25 19:49:18
LastEditTime: 2026-10-25 20:35:13
'''
#
# @lc app=leetcode id=2594 lang=python3
#
# [2594] Minimum Time to Repair Cars
#

# @lc code=start
import math
from collections import Counter
class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:

        # Method: Binary Search
        # time complexity: O(KlogU), K=size(set(ranks)), U=binary search range
        # space complexity: O(1)

        # Use hashmap to reduce the duplicated mechanic ranks
        rank_counts = Counter(ranks)
        # check if the mechanics can repair all cars within `m` minutes
        def check(m):
            cnt = 0
            for r, r_count in rank_counts.items():
                # calculate the cars repaired by `r`, then multiply by machanic count
                cnt += math.isqrt(m // r) * r_count
                if cnt >= cars:
                    return True
            return False

        left = 1
        # if all cars are repaired by the fastest mechanic
        right = min(rank_counts.keys()) * (cars ** 2)
        # binary search to find the smallest `m`
        while left <= right:
            mid = (left + right) // 2
            # if mid is valid, continue searching left side
            if check(mid):
                right = mid - 1
            else:
                left  = mid + 1

        return left
# @lc code=end

