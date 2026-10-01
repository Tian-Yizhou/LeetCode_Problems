'''
Author: Hannah
Date: 2026-10-01 11:15:11
LastEditTime: 2026-10-01 14:07:27
'''
#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#

# @lc code=start
# from functools import cache
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD =  1_000_000_007
        len_g = len(group)

        # Method 3: DP, optimize method 2
        # space complexity: O(n * minProfit)
        dp = [[0] * (minProfit+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, len_g+1):
            member = group[i-1]
            p = profit[i-1]
            for j in range(n, -1, -1):
                for k in range(minProfit, -1, -1):
                    # reverse update because we need old dp[j-member][k-p]
                    if j - member >= 0:
                        dp[j][k] += dp[j-member][max(0, k-p)]

        max_schemes = sum(dp[j][minProfit] for j in range(n+1))

        return max_schemes % MOD

        # Method 2: DP
        # time complexity: O(len_g * n * minProfit)
        # space complexity: O(len_g * n * minProfit)
        dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(len_g+1)]
        dp[0][0][0] = 1

        for i in range(1, len_g+1):
            member = group[i-1]
            p = profit[i-1]
            for j in range(n+1):
                for k in range(minProfit+1):
                    # not select current project
                    dp[i][j][k] = dp[i-1][j][k]
                    # if we have member, we can select this project
                    if j - member >= 0:
                        dp[i][j][k] += dp[i-1][j-member][max(0, k-p)]

        max_schemes = sum(dp[len_g][j][minProfit] for j in range(n+1))

        return max_schemes % MOD

        # Method 1: DP
        # time complexity: O(len_g * n * minProfit)
        # space complexity: O(len_g * n * minProfit)
        # dp(i, n_left, p): the number of profitable schemes 
        # given group[:i+1], with `n_left` members and achieve at least `p` profit
        @cache
        def dp(i, n_left, p):
            # boundary case
            # if all projects are considered
            if i < 0:
                # if required profit is achieved, it is a valid scheme
                return 1 if p == 0 else 0
            
            # don't select current project i
            res = dp(i - 1, n_left, p)
            
            # if we have enough members, we can consider select current project
            if n_left >= group[i]:
                # if the required profit is achieved, we set p to 0 meaning we don't need to achieve any more profit
                res += dp(i - 1, n_left - group[i], max(0, p - profit[i]))
            
            return res
        
        max_schemes = dp(len_g-1, n, minProfit)
        
        return max_schemes % MOD
# @lc code=end

