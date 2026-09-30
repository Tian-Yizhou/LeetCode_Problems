#
# @lc app=leetcode id=3877 lang=python3
#
# [3877] Minimum Removals to Achieve Target XOR
#

# @lc code=start
from functools import cache
from math import inf
class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:

        n = len(nums)

        # Method 2: dp
        

        # Method 1: dfs
        # time complexity: O(nU), U=max_bit(nums)
        # space complexity: O(nU)
        # dfs(i, x): the min removal array nums[:i+1] has XOR value x
        @cache
        def dfs(i, x):
            # boundary
            if i == 0:
                # if x is the value of nums[0], don't remove
                if x == nums[i]:
                    return 0
                # if x is 0, remove nums[0]
                elif x == 0:
                    return 1
                # otherwise, cannot get x, invalid
                else:
                    return inf
            # if nums[i] is removed, dfs(i, x) = dfs(i-1, x) + 1
            # if nums[i] is not removed, dfs(i, x) = dfs(i-1, x^nums[i])
            return min(dfs(i-1, x) + 1, dfs(i-1, x^nums[i]))

        ans = dfs(n-1, target)
        return ans if ans < inf else -1
# @lc code=end

