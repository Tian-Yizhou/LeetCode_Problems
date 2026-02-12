'''
Author: Hannah
Date: 2026-01-27 00:59:30
LastEditTime: 2026-01-27 01:30:57
'''
#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        
        # sort based by scores, for the same score, sort by ages
        players = [[scores[i], ages[i]] for i in range(n)]
        players.sort(key=lambda p: (p[0], p[1]))

        # dp[i]: the max scores of a team when the oldest palyer is ages[i]
        dp = [0] * n

        for i, (s, a) in enumerate(players):
            for j in range(i):
                # if the age of player[j] <= player[i], the team can get at least dp[j] scores
                if players[j][1] <= a:
                    dp[i] = max(dp[i], dp[j])
            # add the score of player[i]
            dp[i] += s
        
        return max(dp)
# @lc code=end

