#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # the XOR of 0 and any number is the number
        ans = 0
        for i in range(n):
            ans = ans ^ (start + i * 2)

        return ans
# @lc code=end

