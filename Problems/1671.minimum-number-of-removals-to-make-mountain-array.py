'''
Author: Hannah
Date: 2026-01-26 21:44:33
LastEditTime: 2026-01-26 23:42:10
'''
#
# @lc app=leetcode id=1671 lang=python3
#
# [1671] Minimum Number of Removals to Make Mountain Array
#

# @lc code=start
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        def get_LIS_len(arr):

            tail = []
            lis_len = [0] * len(arr)
            
            # find the longest LIS if the LIS ends with arr[i]
            for i, num in enumerate(arr):
                idx = bisect_left(tail, num)
                if idx == len(tail):
                    tail.append(num)
                else:
                    tail[idx] = num
                
                # record the length of LIS ends with arr[i]
                lis_len[i] = idx + 1
            
            # return the length of LIS if LIS ends with arr[i]
            return lis_len
        
        n = len(nums)
        # initialize the result as inf, meaning that cannot become a mountain
        mountain_len = [inf] * n

        # the length of LIS ((the left side of nums[i])
        left_lis = get_LIS_len(nums)
        # the length of LDS (the right side of nums[i])
        right_lis = get_LIS_len(nums[::-1])[::-1]

        # for nums[i]
        for i in range(n):
            if left_lis[i] > 1 and right_lis[i] > 1:
                # the number of elements to remove if chose nums[i] as peek
                # add 1 because we count nums[i] twice
                mountain_len[i] = n - left_lis[i] - right_lis[i] + 1

        return min(mountain_len)
# @lc code=end

