'''
Author: Hannah
Date: 2026-09-30 19:36:36
LastEditTime: 2026-09-30 21:32:34
'''
#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
# import bisect
# from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        # Method 2: binary search
        # time complexity: O(n + qlogn)
        # space complexity: O(n)
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        n = len(nums)
        for p in indices.values():
            # insert the first and last element to the head and tail of the list to avoid index out of range
            i0 = p[0]
            p.insert(0, p[-1] - n)
            p.append(i0 + n)

        for idx, query in enumerate(queries):
            p = indices[nums[query]]
            # if the number is unique, we cannot find the closest equal element
            if len(p) == 3:
                queries[idx] = -1
            else:
                j = bisect.bisect_left(p, query)
                queries[idx] = min(query - p[j - 1], p[j + 1] - query)
        return queries

        # Method 1: Time Limit Exceeded
        n = len(nums)
        ans = []
        for query in queries:
            center = nums[query]
            for step in range(1, n//2+1):
                left = (query - step % n + n) % n
                right = (query + step) % n
                if nums[left] == center or nums[right] == center:
                    ans.append(step)
                    break
            else:
                ans.append(-1)

        return ans

# @lc code=end

