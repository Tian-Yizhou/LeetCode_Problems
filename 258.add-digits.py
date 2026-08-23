#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # Method 2: digital root
        if num != 0: # num > 0
            return (num-1) % 9 + 1
        else:
            return 0


        # Mehod 1: while loop
        while num >= 10:
            sum = 0
            while num != 0:
                sum += num % 10
                num //= 10
            num = sum
        return num


# @lc code=end

