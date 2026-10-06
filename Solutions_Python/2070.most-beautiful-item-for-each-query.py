'''
Author: Hannah
Date: 2026-10-06 11:57:43
LastEditTime: 2026-10-06 13:04:34
'''
#
# @lc app=leetcode id=2070 lang=python3
#
# [2070] Most Beautiful Item for Each Query
#

# @lc code=start
# import bisect
class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        
        # Method 1: Binary search
        # time complexity: O((N+Q)logN), N=len(items)
        # space complexity: O(Q), Q = len(queries)
        ans = []
        items.sort(key=lambda x: x[0])
        # calculate prefix max beauty
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])


        for query in queries:
            # find the smallest price > query
            idx_p = bisect.bisect_right(items, query, key=lambda x: x[0])
            # if all the prices are higher than query, beauty is 0
            if idx_p == 0:
                ans.append(0)
            else:
                b = items[idx_p-1][1]
                ans.append(b)

        return ans
# @lc code=end

