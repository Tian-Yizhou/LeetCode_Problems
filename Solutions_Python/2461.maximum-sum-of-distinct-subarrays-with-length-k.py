#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
# from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # time complexity: O(n)
        # space complexity: O(k)
        ans = 0
        cnt = Counter()
        s = 0
        left = 0

        # sliding window
        for right, val in enumerate(nums):
            # add the right end
            cnt[val] += 1
            s += val

            # if element is not distinct, or the length > k, 
            # then move left end
            while cnt[val] > 1 or right - left + 1 > k:
                # move count and sum
                cnt[nums[left]] -= 1
                s -= nums[left]
                # move left pointer
                left += 1

            # if we get a length k sub-array, update answer
            if right - left + 1 == k:
                ans = max(ans, s)

        return ans

                
# @lc code=end

