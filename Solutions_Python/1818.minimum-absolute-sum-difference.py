'''
Author: Hannah
Date: 2026-10-02 14:03:20
LastEditTime: 2026-10-02 14:50:46
'''
#
# @lc app=leetcode id=1818 lang=python3
#
# [1818] Minimum Absolute Sum Difference
#

# @lc code=start
import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        MOD = 1_000_000_007
        # Method: Binary Search
        # time complexity: O(nlogn)
        # space complexity: O(n)
        
        n = len(nums1)
        arr = sorted(nums1)
        s = sum([abs(nums1[i] - nums2[i]) for i in range(n)])
        max_reduction = 0
        for i in range(n):
            original_diff = abs(nums1[i] - nums2[i])
            # if the diff is already 0, no need to replace
            if original_diff == 0:
                continue

            # find the element in nums1 that closest to nums2[i]
            target = nums2[i]
            idx = bisect.bisect_left(arr, nums2[i])

            # the element >= target 
            if idx < n:
                new_diff = abs(arr[idx] - target)
                max_reduction = max(max_reduction, original_diff - new_diff)
            # the element < target
            if idx > 0:
                new_diff = abs(arr[idx-1] - target)
                max_reduction = max(max_reduction, original_diff - new_diff)

        return (s - max_reduction) % MOD


# @lc code=end

