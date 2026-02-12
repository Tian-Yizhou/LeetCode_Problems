#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Method 1: Dynamic Programming
        # dp[i]: the length of longest strictly increasing subsequence of nums[:i]
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j], dp[i])
            
            dp[i] += 1
        
        return max(dp)
# @lc code=end

