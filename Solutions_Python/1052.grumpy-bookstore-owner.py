#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # time complexity: O(n)
        # space complexity: O(1)
        # separate the satisfied cutomers when the owner is grumpy and not grumpy
        # our target is to find max s_grumpy
        s_grumpy, s_not_grumpy = 0, 0
        max_s_grumpy = 0
        for i, c in enumerate(grumpy):
            if c == 1:
                s_grumpy += customers[i]
                max_s_grumpy = max(max_s_grumpy, s_grumpy)
            else:
                s_not_grumpy += customers[i]

            # sliding the window
            left = i - minutes + 1
            if left >= 0:
                if grumpy[left] == 1:
                    s_grumpy -= customers[left]

        return max_s_grumpy + s_not_grumpy
            

        
# @lc code=end

