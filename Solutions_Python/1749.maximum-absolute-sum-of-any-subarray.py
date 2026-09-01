#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        # Method 3: dp, optimize method 2 space complexity to O(1)
        # time complexity: O(n)
        # space complexity: O(1)
        # f[i]: the max_abs sub-array sum of sub-array ends with nums[i]
        n = len(nums)
        ans = 0
        pre_sum = 0
        max_pre_sum, min_pre_sum = 0, 0
        for i, num in enumerate(nums):
            pre_sum += num
            min_pre_sum = min(min_pre_sum, pre_sum)
            max_pre_sum = max(max_pre_sum, pre_sum)
            ans = max(max_pre_sum - min_pre_sum, ans)

        return ans
    
        # Method 2: dp
        # time complexity: O(n)
        # space complexity: O(n)
        # f[i]: the max_abs sub-array sum of sub-array ends with nums[i]
        n = len(nums)
        f = [0] * n
        pre_sum = 0
        max_pre_sum, min_pre_sum = 0, 0
        for i, num in enumerate(nums):
            pre_sum += num
            min_pre_sum = min(min_pre_sum, pre_sum)
            max_pre_sum = max(max_pre_sum, pre_sum)
            f[i] = max_pre_sum - min_pre_sum

        return max(f)
            
        
        # Method 1: pre sum + greedy
        # time complexity: O(n)
        # space complexity: O(1)
        # max_abs sum of sub-array = max_pre_sum - min_pre_sum
        ans = 0
        pre_sum = 0
        min_pre_sum, max_pre_sum = 0, 0

        for num in nums:
            pre_sum += num
            # update min and max pre_sum
            min_pre_sum = min(min_pre_sum, pre_sum)
            max_pre_sum = max(max_pre_sum, pre_sum)
            # update answer
            ans = max(max_pre_sum - min_pre_sum, ans)

        return ans
# @lc code=end

