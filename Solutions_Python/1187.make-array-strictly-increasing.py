'''
Author: Hannah
Date: 2026-01-27 01:31:32
LastEditTime: 2026-01-28 11:30:59
'''
#
# @lc app=leetcode id=1187 lang=python3
#
# [1187] Make Array Strictly Increasing
#

# @lc code=start
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2 = sorted(set(arr2))
        n1, n2 = len(arr1), len(arr2)

        # Method 2

        arr1 = arr1 + [inf]

        # dfs(i): the longest strictly increasing subsequence of arr1[:i+1] (ends with arr1[i])
        # arr1[i] is not substituted. Given arr1[j] that is also not substituted,
        # if we can substitue arr1[j+1:i] with a sub-array of arr2, then arr[:i+1] is strictly increasing
        @cache
        def dfs(i):
            # if i==0, no operation needed
            # find the largest number in arr2 that lower than arr1[i]
            idx = bisect_left(arr2, arr1[i])
            if idx >= i:
                res = 0
            else:
                res = -inf
            
            if i and arr1[i-1] < arr1[i]:
                res = max(res, dfs(i-1))
            
            for j in range(i-2, max(i-idx-2, -1), -1):
                if arr2[idx - (i-j-1)] > arr1[j]:
                    res = max(res, dfs(j))
            
            return res + 1
        
        ans = dfs(n1)

        return n1+1-ans if ans >= 0 else -1



        # # Method 1
        # # dfs(i, pre): operations needed to make arr1[:i+1] (ends with arr1[i]), arr[i+1]=pre strictly inceasing
        # @cache
        # def dfs(i, pre):
        #     # if there is no number, no operation needed
        #     if i < 0:
        #         return 0
        #     # if we don't substitute arr1[i], 
        #     # the operations needed eaul making arr1[:i] strictly increasing
        #     # if arr1[i] < pre, arr[:i+2] is strictly increasing
        #     if arr1[i] < pre:
        #         res = dfs(i-1, arr1[i])
        #     # if arr[i] >= pre, arr[:i+2] is illegal
        #     else:
        #         res = inf
            
        #     # if we substitute arr1[i]
        #     # find the largest number among numbers lower than pre
        #     idx = bisect_left(arr2, pre) - 1
        #     # if we can find one
        #     if idx >= 0:
        #         # substitue arr1[i] with arr2[idx], operations add 1
        #         res2 = dfs(i-1, arr2[idx]) + 1
            
        #         # choose the way needs fewer operations
        #         res = min(res, res2)
            
        #     return res
        
        # # assume there is a number arr1[n1], and it is inf
        # # meaning that arr1[n1-1] always smaller than its next number
        # ans = dfs(n1-1, inf)

        # return ans if ans < inf else -1
            
# @lc code=end

Solution.makeArrayIncreasing([1,5,3,6,7], [1,3,2,4])
