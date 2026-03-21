'''
Author: Hannah
Date: 2026-03-21 14:36:42
LastEditTime: 2026-03-21 15:15:38
'''
#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start

# from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        ans = 0

        # expand the window starting from idx=0
        left = 0

        # queue record the idx of max num in a window(subarray)
        max_q = deque()
        min_q = deque()

        for i, num in enumerate(nums):
            # update the max number and min number of subarray
            while max_q and num >= nums[max_q[-1]]:
                max_q.pop()
            # it doesn't matter if we temporarily add i into max_q
            max_q.append(i)
            while min_q and num <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            # ensure current subarray is legal
            # if the range exceed limit
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                # move left boundary
                left += 1
                # if min number is out of the window
                if min_q[0] < left:
                    min_q.popleft()
                # if max number is out of window
                if max_q[0] < left:
                    max_q.popleft()
            # after the while loop, the subarray is legal
            # update max subarray length
            ans = max(ans, i-left+1)
        
        return ans
# @lc code=end

