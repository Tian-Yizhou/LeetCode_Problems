'''
Author: Hannah
Date: 2026-10-29 11:25:07
LastEditTime: 2026-10-29 12:05:13
'''
#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        # Method: Binary Search
        # time complexity: O(NlogU), N=len(bloomDay), U=max(bloomDay)
        # space complexity: O(1)

        n = len(bloomDay)
        # if we cannot make m bouquets
        if n < m * k:
            return -1

        # at `mid` day, can we make m bouquet? True
        def check(mid: int) -> bool:
            # count bouquets and consecutive bloom flowers
            bouquets = 0
            consecutive = 0
            # one loop, greedy
            for day in bloomDay:
                # if current flower is bloom, consecutive add 1
                if day <= mid:
                    consecutive += 1
                    # if it's enough to make a bouquet
                    if consecutive == k:
                        # update bouquet and reset consecutive
                        bouquets += 1
                        consecutive = 0
                        if bouquets >= m:
                            return True
                # if current flower is not bloom, reset consecutive
                else:
                    consecutive = 0
                    
            return False

        # the boundary of binary search
        left, right = 0, max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            # if `mid` is valid, continue searching left side
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
# @lc code=end

