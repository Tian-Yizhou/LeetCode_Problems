#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Method 3: optimize the space complexity of method 2 to O(1)
        # in fact, we only need two variables
        n = len(nums)
        ans = nums[0]
        f_0 = nums[0]
        for i in range(1, n):
            f_1 = max(f_0, 0) + nums[i]
            ans = max(ans, f_1)
            f_0 = f_1

        return ans


        # Method 2: concat nums[i] with left side or not
        # time complexity: O(n)
        # space complexity: O(n)
        n = len(nums)
        # f[i]: the max sub-array sum that ends with nums[i]
        # if f[i-1]<0, then f[i-1] + nums[i] < nums[i], don't cancat;
        # if f[i-1]>0, then f[i-1] + nums[i] > nums[i], cancat
        f = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                f[i] = nums[i]
            else:
                f[i] = max(f[i-1], 0) + nums[i]

        # the max sub-array sum could end with any nums[i]
        return max(f)

        # Method 1: max sub-array sum = pre_sum - min_pre_sum
        # time complexity: O(n)
        # space complexity: O(1)
        ans = -inf
        pre_sum, min_pre_sum = 0, 0

        for num in nums:
            # update pre_sum
            pre_sum += num
            # update answer
            ans = max(ans, pre_sum - min_pre_sum)
            # update min_pre_sum
            min_pre_sum = min(min_pre_sum, pre_sum)

        return ans
# @lc code=end

