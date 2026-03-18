'''
Author: Hannah
Date: 2026-03-18 00:12:08
LastEditTime: 2026-03-18 00:42:42
'''
#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = {x:i for i, x in enumerate(nums1)}
        n1 = len(nums1)
        ans = [-1] * n1
        ms = []

        for i, x in enumerate(nums2):
            while ms and x > ms[-1]:
                ans[record[ms.pop()]] = x
            if x in record:
                ms.append(x)
        
        return ans


# @lc code=end

