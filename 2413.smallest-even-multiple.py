#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # if the number is odd
        if n % 2 == 1:
            return n * 2
        # if the number is even
        else:
            return n
# @lc code=end

