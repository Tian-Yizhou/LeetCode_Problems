'''
Author: Hannah
Date: 2026-03-21 18:15:09
LastEditTime: 2026-03-21 20:44:45
'''
#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start

# from typing import List
# from math import inf
# from itertools import accumulate
# from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Method: Monotonic queue
        ans = inf
        # calculate sum of nums[:i+1]
        s = list(accumulate(nums, initial=0))
        # use a queue containing the sum of nums[:i+1]
        q = deque()

        # given a pre_fix sum, s[i]
        for i, cur_s in enumerate(s):
            # if q is not empty, and
            # the sum of subarray satisfies condition
            while q and cur_s - s[q[0]] >= k:
                # update answer;
                # q[0] is not needed because we cannot find a shorter subarray
                # for a later pre_fix and subarray nums[q[0]:i+1]
                ans = min(ans, i - q.popleft())
            # if q is not empty
            # if previous pre_fix sum s[q[-1]] >= s[i]
            # then s[q[-1]] is not needed
            # because if any later pre_fix can satisfies condition
            # with s[q[-1]], it can also satisfies condition with s[i]
            while q and s[q[-1]] >= cur_s:
                q.pop()
            q.append(i)
        
        return ans if ans < inf else -1
        
# @lc code=end

