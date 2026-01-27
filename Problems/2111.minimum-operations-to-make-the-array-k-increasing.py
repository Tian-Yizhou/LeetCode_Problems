'''
Author: Hannah
Date: 2026-01-26 21:44:38
LastEditTime: 2026-01-26 22:54:39
'''
#
# @lc app=leetcode id=2111 lang=python3
#
# [2111] Minimum Operations to Make the Array K-Increasing
#

# @lc code=start
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        ans = 0
        
        # divide the arr into k sub arrs
        for i in range(k):
            sub_arr = arr[i:n:k]
            sub_n = len(sub_arr)

            # for each sub arr, find the longest non-decreasing subsequence
            # then the numbers need modified are those not included in the longest subsequence
            tails = []
            for j, x in enumerate(sub_arr):
                idx = bisect_right(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
            # add the nums need to be modified to answer
            ans += (sub_n - len(tails))
        
        return ans


# @lc code=end

