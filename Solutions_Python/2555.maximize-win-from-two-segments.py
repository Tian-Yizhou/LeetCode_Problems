#
# @lc app=leetcode id=2555 lang=python3
#
# [2555] Maximize Win From Two Segments
#

# @lc code=start
class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        n = len(prizePositions)
        # Method 1: Sliding window + DP
        # time complexity: O(N)
        # space complexity: O(N)
        # use sliding window to get the #prizes of second segment,
        # and maintain the max #prizes of the first segment

        # if k is large enough to cover the whole array, all elements can be picked
        if k * 2 >= prizePositions[-1] - prizePositions[0]:
            return n

        # dp[i]: the max #prizes of prizePositions[:i]
        dp = [0] * (n+1)
        ans = 0
        # iterate every right end of the second segment,
        # then #prizes = dp[left] + (right-left+1)
        left = 0
        for right in range(n):
            # if second segment length > k, move left end
            while prizePositions[right]-prizePositions[left] > k:
                left += 1
            # now the window is valid, update answer
            ans = max(ans, dp[left]+right-left+1)
            # udpate dp, note dp has n+1 elements so use right+1
            dp[right+1] = max(dp[right], right-left+1)

        return ans
            
        
# @lc code=end

