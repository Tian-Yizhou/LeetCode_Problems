'''
Author: Hannah
Date: 2026-02-01 11:25:53
LastEditTime: 2026-02-14 14:22:56
'''
#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        
        # Method 2: open interval
        # the minimal valid h-index is 0
        left = 0
        # the minimal invalid h-index is min(len(citations), max(citations)) + 1
        right = min(n, max(citations)) + 1

        while left + 1 < right:
            mid = (left + right) // 2
            if citations[-mid] >= mid:
                left = mid
            else:
                right = mid
        
        return left

        # Method 1: close interval
        # the range of valid h-index is [0, min(len(citations), max(citations))]
        left = 0
        right = min(n, max(citations))

        while left <= right:
            # mid is the h-index value
            mid = (left + right) // 2
            # if there are more than h papers have citation greater than h
            # This also works: if n - bisect_left(citations, mid) >= mid:
            if citations[-mid] >= mid:
                # mid is currently the biggest h-index
                left = mid + 1
            # else currently biggest h-index is less than mid
            else:
                right = mid - 1
        
        return right
        
# @lc code=end

