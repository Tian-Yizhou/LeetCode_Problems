'''
Author: Hannah
Date: 2026-02-01 11:25:07
LastEditTime: 2026-02-13 00:47:05
'''
#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Method 2: bisect
        arr2.sort()
        n = len(arr2)
        ans = 0
        for x in arr1:
            # find the min arr2[j] s.t arr2[j] >= (x-d)
            idx = bisect_left(arr2, x-d)
            # if j exceed arr2, or arr2[j] > x+d
            if idx == n or arr2[idx] > x+d:
                # then no numbers in arr2 satisfy x-d <= arr2[j] <= x+d
                ans += 1
        
        return ans



        # Method 1: two pointers
        # arr1.sort()
        # arr2.sort()
        # ans = 0
        # j = 0
        # for x in arr1:
        #     # find the min arr2[j] s.t arr2[j] >= (x-d)
        #     while j < len(arr2) and arr2[j] < x - d:
        #         j += 1
        #     # we find arr2[j], if j exceed arr2, or arr2[j] > x+d
        #     if j == len(arr2) or arr2[j] > x + d:
        #         # then no numbers in arr2 satisfy x-d <= arr2[j] <= x+d
        #         ans += 1
        # return ans

# @lc code=end

