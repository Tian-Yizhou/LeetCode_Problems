'''
Author: Hannah
Date: 2026-02-01 11:31:38
LastEditTime: 2026-03-23 20:59:29
'''
#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#

# @lc code=start

# from math import inf

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        # Method: Dynamic Programming
        # fix two vertices i, j, move (clockwise) a vertice k from i+1 to j-1
        # for each k, vertices i to k consist a sub-polygon, 
        # vertices k to j consist another sub-polygon
        # so we need a function to find the min score of a polygon given two vertices

        # Method 2: use array
        n = len(values)
        dp = [[0]*n for _ in range(n)]

        # i starts from n-1 because j will take one vertice
        for i in range(n-2, -1, -1):
            # j is at least one vertice later than i
            for j in range(i+1, n):
                # if i starts from n-3, we can get rid of this judge
                if i+1 == j:
                    dp[i][j] = 0
                else:
                    score = inf
                    for k in range(i+1, j):
                        score = min(score, dp[i][k] + dp[k][j] + values[i]*values[k]*values[j])
                    dp[i][j] = score
        return dp[0][n-1]

        # Method 1: use cache
        # dp(i, j): return the min score of a polygon consist of vertices i to j
        @cache
        def dp(i, j):
            # cannot construct a triangle
            if i+1 == j:
                return 0
            # set initial answer
            ans = inf
            # for each vertice between i and j
            for k in range(i+1, j):
                # update answer
                ans = min(ans, dp(i, k) + dp(k, j) + values[i]*values[j]*values[k])
            
            return ans
        
        n = len(values)

        return dp(0, n-1)

# @lc code=end

