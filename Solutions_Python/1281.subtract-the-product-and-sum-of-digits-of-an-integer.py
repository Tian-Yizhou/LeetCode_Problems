#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mult = 1
        s = 0
        while n != 0:
            num = n % 10
            # update mult and s
            mult *= num
            s += num
            # update n
            n = n // 10

        return mult - s
# @lc code=end

