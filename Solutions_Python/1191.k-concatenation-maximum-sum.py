'''
Author: Hannah
Date: 2026-09-24 12:30:09
LastEditTime: 2026-09-25 00:41:24
'''
#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#

# @lc code=start
class Solution:
    # a function to find the max sub-array sum of a nums list repeated `repeat` times
    def maxSubArray(self, nums, repeat):
        ans = 0
        cur = 0
        for _ in range(repeat):
            for num in nums:
                cur = max(cur, 0) + num
                ans = max(ans, cur)
        return ans
            
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD = 1_000_000_007

        # Method 2: DP, optimize space complexity to O(1)
        # time complexity: O(n)
        # space complexity: O(1)

        # if the arr only duplicate once
        if k == 1:
            max_sum = self.maxSubArray(arr, 1)
            return max_sum % MOD
        # if the arr duplicate more than once, we only need to 
        # duplicate it twice to find the max sum of sub-array
        max_sum = self.maxSubArray(arr, 2)
        # if the max sum of sub-array appears within the arr, then max_sum is the answer
        # if the max sum of sub-array appears across the arr, then we need to add the sum of arr * (k-2)
        max_sum = max_sum + max(0, sum(arr)) * (k - 2)

        return max_sum % MOD


        # Method 1: DP, but Memory Limit Exceeded
        # time complexity: O(n), n is the length of arr after duplicate it k times
        # space complexity: O(n)
        # dp[i]: the max sub-array sum of arr[:i+1]
        max_sum = max(0, arr[0])
        dp = [max_sum]
        # the arr[i] can join the sub-array end with arr[i-1], 
        # or start a new sub-array by itself
        for i in range(1, n):
            dp.append(max(dp[i-1]+arr[i], arr[i]))
            max_sum = max(max_sum, dp[i])

        return max_sum % MOD


# @lc code=end

