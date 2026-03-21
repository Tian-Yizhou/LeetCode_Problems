'''
Author: Hannah
Date: 2026-03-21 11:16:56
LastEditTime: 2026-03-21 12:39:31
'''
#
# @lc app=leetcode id=2320 lang=python3
#
# [2320] Count Number of Ways to Place Houses
#

# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:

        # Method 4: like 198. house robber
        # boundary: f[0] is the methods to set house on i-2 plot;
        # f[1] is the methods t set house on i-1 plot
        f = [1, 2]
        
        # start from the second plot (idx=1)
        for i in range(1, n):
            # record f[i-1]
            pre = f[1]
            # if don't set a house on plot i, we have f[i-1] methods
            # if set a house on plot i, we have f[i-2] methods
            # so for plot i, we have f[i-1] + f[i-2] methods in total
            f[1] = f[0] + f[1]
            # update f[i-2]
            f[0] = pre
        
        return f[1] ** 2 % (10**9 + 7)

        # Method 3: optimization of method 2
        house_1, house_0 = 0, 1
        for i in range(n):
            pre_house_1 = house_1
            # update house_1
            house_1 = house_0
            # update house_0
            house_0 = house_0 + pre_house_1
        
        ans = (house_0 + house_1) ** 2 % (10**9 + 7)

        return ans

        # Method 2: use array to store the result
        # initialization included
        house_1 = [0] * (n + 1)
        house_0 = [1] * (n + 1)

        for i in range(n):
            house_1[i+1] = house_0[i]
            house_0[i+1] = house_0[i] + house_1[i]
        
        ans = (house_1[-1] + house_0[-1]) ** 2 % (10**9 + 7)

        return ans

        # Method 1
        # dp(i, s): the methods of plot i with status s
        # s=0: no house on plot i; s=1 set house on i
        @cache
        def dp(i, s):
            # boundary: if there is no plot
            if i < 0:
                # impossible to set a house without plot
                if s == 1:
                    return 0
                # only 1 method: no plot, no house
                else:
                    return 1
            # for i >= 0
            # if set a house on i-th plot
            if s == 1:
                # (i-1) must be empty
                return dp(i-1, 0)
            # if i-th plot is empty
            else:
                # (i-1) could have a house or not
                return dp(i-1, 1) + dp(i-1, 0)
        
        ans = (dp(n-1, 0) + dp(n-1, 1)) ** 2 % (10**9 + 7)

        return ans


        
# @lc code=end

