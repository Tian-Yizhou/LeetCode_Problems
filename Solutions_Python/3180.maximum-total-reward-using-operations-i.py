'''
Author: Hannah
Date: 2026-09-27 09:51:19
LastEditTime: 2026-09-27 10:58:14
'''
#
# @lc app=leetcode id=3180 lang=python3
#
# [3180] Maximum Total Reward Using Operations I
#

# @lc code=start
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # the order of rewards doesn't matter so we can sort
        nums = sorted(set(rewardValues))
        # the total reward will be no larger than 2m-1
        m = nums[-1]

        # Method 1: DP
        # time complexity: O(nlogn + n*M), n is #set(rewardValues)
        # space complexity: O(M), M is the max reward in rewardValues
        # dp(i, r): can we get `r` reward from rewardValues[:i+1]
        dp = [False] * (2 * m)
        dp[0] = True
        ans = nums[0]

        for r in nums:
            for j in range(r-1, -1, -1):
                if dp[j] is True:
                    dp[j+r] = True
                    ans = max(j+r, ans)

        return ans

# @lc code=end

