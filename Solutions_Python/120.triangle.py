#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
# from functools import cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # Method 3: dp, bottom to top
        # time complexity: O(N), N is the number of elements
        # space complexity: O(n), n is the number of rows
        m = len(triangle)
        dp = triangle[-1].copy()

        # upper layer's dp[j] could be 
        # arrived from current layer's dp[j] or dp[j+1]
        for i in range(m-2, -1, -1):
            row_len = len(triangle[i])
            for j in range(row_len):
                # rewrite dp[j] from left to right
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
                # or we can use dp[j-1] and rewrite from left to right
                # for j in range(m-1, m-1-row_len, -1):
                # dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
                # return dp[-1]

        return dp[0]


        # Method 2: dp, top to bottom
        # time complexity: O(N), N is the number of elements
        # space complexity: O(n), n is the number of rows
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]

        # note: the i-th row has i elements
        for i in range(1, n):
            # backward update
            for j in range(i, -1, -1):
                # update right boundary first
                if j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                # update left boundary last
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]

        # dp contains the sum of last row
        return min(dp)


        # Method 1: dfs
        # time complexity: O(N), N = the number of elements
        # space complexity: O(N)
        m, n = len(triangle), len(triangle[-1])

        # dfs(i, j): the min path sum to arrive triangle[i][j]
        @cache
        def dfs(i, j):
            # if it's start, the sum is itself
            if i == 0:
                return triangle[0][0]
            # if it's boundary, it can only be arrived from one element
            row_len = len(triangle[i])
            # left boundary
            if j-1 < 0:
                return dfs(i-1, j) + triangle[i][j]
            # right boundary
            if j == row_len-1:
                return dfs(i-1, j-1) + triangle[i][j]
            return min(dfs(i-1, j-1), dfs(i-1, j)) + triangle[i][j]

        return min(dfs(m-1, j) for j in range(n))

# @lc code=end

