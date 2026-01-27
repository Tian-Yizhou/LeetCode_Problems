'''
Author: Hannah
Date: 2026-01-27 01:00:11
LastEditTime: 2026-01-27 01:00:23
'''
#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        # sort envelopes based on width.
        # for same width, sort the height in decending order
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        
        n = len(envelopes)
        # max_envs[:i+1]: the max envelopes if we choose envelopes[i] as the biggest
        max_envs = []

        # binary search
        for w, h in envelopes:
            idx_h = bisect_left(max_envs, h)
            if idx_h  == len(max_envs):
                max_envs.append(h)
            else:
                max_envs[idx_h] = h
        
        return len(max_envs)
# @lc code=end

