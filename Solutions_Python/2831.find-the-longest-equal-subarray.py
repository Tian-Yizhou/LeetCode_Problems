'''
Author: Hannah
Date: 2026-10-07 17:07:23
LastEditTime: 2026-10-07 17:35:50
'''
#
# @lc app=leetcode id=2831 lang=python3
#
# [2831] Find the Longest Equal Subarray
#

# @lc code=start
# from collections import defaultdict
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # Method: Sliding window
        # time complexity: O(N), N is len(nums)
        # space complexity: O(N)
        # for each unique number in nums, assume it is the target equal subarray
        # record all the indices of one number, check what is the longest length
        idx_lists = defaultdict(list)
        for i, num in enumerate(nums):
            idx_lists[num].append(i)

        ans = 0
        # for each numnber, use sliding window to find the max valid subarray
        for idx_list in idx_lists.values():
            # the window size is l1 = right-left+1, it's also the count of equal elements
            # the subarray length before delete is l2 = idx_list[right]-idx_list[left]+1
            # the count of elements need to be deleted is l2 - l1
            left = 0
            for right, idx in enumerate(idx_list):
                while (idx_list[right] - idx_list[left]) - (right-left) > k:
                    left += 1
                # when the subarray is valid, update answer
                ans = max(ans, right-left+1)

        return ans
                

# @lc code=end

