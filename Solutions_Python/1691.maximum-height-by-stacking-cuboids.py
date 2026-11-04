'''
Author: Hannah
Date: 2026-11-03 10:31:44
LastEditTime: 2026-11-03 20:02:27
'''
#
# @lc app=leetcode id=1691 lang=python3
#
# [1691] Maximum Height by Stacking Cuboids 
#

# @lc code=start
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:

        # Method: DP
        # time complexity: O(n^2)
        # space complexity: O(n)
        # sort each cuboid's each edge, then we get an ascending array
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()

        n = len(cuboids)
        # dp[i]: consider cuboids[i], choose or not choose
        dp = [0] * n

        for i, (w_i, l_i, h_i) in enumerate(cuboids):
            # iterate through all smaller cuboid
            for j, (w_j, l_j, h_j) in enumerate(cuboids[:i]):
                # if j's length and height are smaller, j can be placed on i
                if l_j <= l_i and h_j <= h_i:
                    # find the j-th cuboid has largest height
                    dp[i] = max(dp[j], dp[i])

            # add the height of i-th cuboid
            dp[i] += h_i
        
        return max(dp)

        
# @lc code=end

