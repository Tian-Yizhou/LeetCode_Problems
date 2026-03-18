'''
Author: Hannah
Date: 2026-03-18 00:43:45
LastEditTime: 2026-03-18 01:28:28
'''
#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        ms = []

        for i in range(n-1, -1, -1):
            while ms and ms[-1] < heights[i]:
                ms.pop()
                ans[i] += 1
            if ms:
                ans[i] += 1
            ms.append(heights[i])
        
        return ans
# @lc code=end

