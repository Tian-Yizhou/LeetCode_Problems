'''
Author: Hannah
Date: 2026-10-02 10:35:57
LastEditTime: 2026-10-02 12:28:10
'''
#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#

# @lc code=start
class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:

        # convert the problem: divide the rods into pile A and pile B
        # find the max sum that A and B can achieve simultaneously
        n = len(rods)
        total_sum = sum(rods)
        capacity = int(total_sum / 2)
        # given a rod, it is in either A or B
        # dp{diff, h}: the height difference is diff, the shorter pile height is h, given rod[:i+1]
        dp = {0: 0}
        for h in rods:
            next_dp = dp.copy()
            for diff, shorter_height in dp.items():
                # put the rod in higher pile
                new_diff_1 = diff + h
                next_dp[new_diff_1] = max(next_dp.get(new_diff_1, 0), shorter_height)
                
                # put the rod in shorter pile
                # the new height difference is abs(diff - h)
                # the shorter pile height will increase min(diff, h)
                new_diff_2 = abs(diff - h)
                new_shorter_height = shorter_height + min(diff, h)
                next_dp[new_diff_2] = max(next_dp.get(new_diff_2, 0), new_shorter_height)
                
            # update dp
            dp = next_dp
            
        # find the max height when difference is 0
        return dp.get(0, 0)

        
        
# @lc code=end

