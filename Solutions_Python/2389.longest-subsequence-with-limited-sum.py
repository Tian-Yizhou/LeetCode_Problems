'''
Author: Hannah
Date: 2026-09-30 19:22:32
LastEditTime: 2026-09-30 19:36:04
'''
#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
# import bisect
class Solution:

    # self-defined bisect_right. Find the smallest index s.t. arr[idx] > x
    def upper_bound(self, arr, x):
        n = len(arr)
        left, right = 0 , n-1
        while left <= right:
            mid = (left + right) // 2
            # when arr[mid] = x, continue search mid's right
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1

        return left
    
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:

        # Method: bisect_right
        # time complexity: O(NlogN + QlogN)
        # space complexity: O(N+Q)
        
        # becuase it's sum of subsequence, so order doesn't matter
        # so we can sort the nums
        nums.sort()
        # greedy: each time we should add the smallest element,
        # so that we can find max length subsequence. So we can use prefix_sum
        s = 0
        prefix_sum = []
        for num in nums:
            s += num
            prefix_sum.append(s)
        # use bisect_right to find the smallest index s.t. prefix_sum[idx] > queries[i]
        # then `idx` is the max length of subsequence
        ans = []
        for query in queries:
            ans.append(self.upper_bound(prefix_sum, query))
            # or we can use bisect_right package
            # ans.append(bisect.bisect_right(prefix_sum, query))

        return ans
        
# @lc code=end

