#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # time complexity: O(n)
        n = len(nums)
        # initialize window
        s = 0
        for i in range(k):
            s += nums[i]
        ans = s / k
        left, right = 0, k-1
        cur_avg = ans

        while right < n-1:
            # update average
            delta = (nums[right+1] - nums[left]) / k
            cur_avg += delta
            # update answer
            ans = max(cur_avg, ans)
            # move window
            left += 1
            right += 1

        return ans


# @lc code=end

