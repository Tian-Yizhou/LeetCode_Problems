#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        # Method 2
        # time complexity: O(n), n status
        # space complexity: O(n), store n status
        # f[i]: the max points we can get in questions[i:]
        f = [0] * (n+1)
        for i in range(n-1, -1, -1):
            # if we solve question i
            idx = min(i + questions[i][1] + 1, n)
            points_1 = questions[i][0] + f[idx]
            # if we don't solve question i
            points_2 = f[i+1]
            f[i] = max(points_1, points_2)

        return f[0]

        # Method 1
        # time complexity: O(n), n status
        # space complexity: O(n), store n status
        # dp(i): the max points we can get in questions[i:]
        @cache
        def dp(i):
            # the boundary is n-1; when there is no question, we can get 0 points
            if i > n-1:
                return 0
            # if we solve question i, then question list becomes quesitons[i+brainpower_i+1:]
            points_1 = questions[i][0]+ dp(i+questions[i][1]+1)
            # if we don't solve question i, then quesiton list becomes questions[i+1:]
            points_2 = dp(i+1)
            return max(points_1, points_2)

        return dp(0)
    
# @lc code=end

