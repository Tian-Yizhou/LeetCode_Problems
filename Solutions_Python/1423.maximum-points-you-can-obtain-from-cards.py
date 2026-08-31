#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
# from math import inf
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # time complexity: O(n)
        # the max points = total points - min_window_points
        total_points = sum(cardPoints)
        n = len(cardPoints)
        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        ans = total_points - window_sum

        # sliding the window
        for i in range(window_size, n):
            window_sum = window_sum + cardPoints[i] - cardPoints[i-window_size]
            ans = max(ans, total_points - window_sum)

        return ans
# @lc code=end

