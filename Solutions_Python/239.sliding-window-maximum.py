'''
Author: Hannah
Date: 2026-03-21 14:14:38
LastEditTime: 2026-03-21 14:35:06
'''
#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

# from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # maintain a stack containing the indices of decreasing number
        q = deque()
        
        for i, num in enumerate(nums):
            # while q is not empty, and current number >= previous number
            while q and num >= nums[q[-1]]:
                # nums[q[-1]] must not be the largest number in this window
                q.pop()
            # add the index of nums[i] into queue
            q.append(i)

            # maintain the window size
            if i - q[0] + 1 > k:
                # remove the first element
                q.popleft()
            
            # record the largest number in this window
            # only record if the window size is k
            if i >= k-1:
                ans.append(nums[q[0]])
        
        return ans
# @lc code=end

