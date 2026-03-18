'''
Author: Hannah
Date: 2026-03-17 22:48:42
LastEditTime: 2026-03-17 23:09:50
'''
#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        ans = [0] * n
        ms = []

        # Method 2: increasing, maintain a stack in which 
        # all elements haven't find a higher temperature
        for i, t in enumerate(temperatures):
            while ms and t > temperatures[ms[-1]]:
                j = ms.pop()
                ans[j] = i - j
            ms.append(i)

        return ans

        # Method 1: backward, maintain a decreasing stack
        # given the temperature of i-th day
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            # if ms is not empty and t >= the last element
            while ms and t >= temperatures[ms[-1]]:
                # remove the last element
                ms.pop()
            # until the ms is a decreasing list
            if ms:
                # we find the first temperature > t
                ans[i] = ms[-1] - i
            ms.append(i)
        
        return ans

        
# @lc code=end

