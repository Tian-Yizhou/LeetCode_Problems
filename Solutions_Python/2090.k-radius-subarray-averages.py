#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # time complexity: O(n)
        n = len(nums)
        ans = [-1] * n
        window_size = 2 * k + 1
        # corner case
        if window_size > n:
            return ans

        # initialize
        window_sum = sum(nums[:window_size])
        ans[k] = window_sum // window_size

        # sliding window: i is the right end
        for i in range(window_size, n):
            window_sum = window_sum + nums[i] - nums[i - window_size]
            ans[i - k] = window_sum // window_size

        return ans
# @lc code=end

