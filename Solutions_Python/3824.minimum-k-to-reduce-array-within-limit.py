'''
Author: Hannah
Date: 2026-10-29 21:34:43
LastEditTime: 2026-10-29 22:02:41
'''
#
# @lc app=leetcode id=3824 lang=python3
#
# [3824] Minimum K to Reduce Array Within Limit
#

# @lc code=start
from math import sqrt, ceil
class Solution:
    def minimumK(self, nums: List[int]) -> int:

        # Method: Binary Search
        # time complexity: O(NlogU), N=len(nums), U=max(nums)
        # space complexity: O(1)

        # check if k=m is valid
        def check(m):
            ops = 0
            for num in nums:
                # num/k <= op
                ops += (num-1)//m + 1
                if ops > m**2:
                    return False
            return True

        # the boundary of binary search
        n = len(nums)
        left, right = ceil(sqrt(n)), max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
# @lc code=end

