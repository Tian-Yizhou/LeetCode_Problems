#
# @lc app=leetcode id=2841 lang=python3
#
# [2841] Maximum Sum of Almost Unique Subarray
#

# @lc code=start
# from collections import Counter
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # time complexity: O(n)
        # space complexity: O(k)
        ans = 0
        cnt = Counter()
        s = 0

        for right, val in enumerate(nums):
            # add new right end element
            cnt[val] += 1
            s += val

            # if the length < k
            left = right - k + 1
            if left < 0:
                continue

            # if # distinct elements >= m, update answer
            if len(cnt) >= m:
                ans = max(ans, s)

            # move the left end
            out_val = nums[left]
            s -= out_val
            cnt[out_val] -= 1
            # clear out value in cnt
            if cnt[out_val] == 0:
                del cnt[out_val]

        return ans
# @lc code=end

