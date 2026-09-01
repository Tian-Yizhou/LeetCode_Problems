#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # Method 3: dp, optimize method 2 space complexity to O(n)
        # time complexity: O(mn)
        # space complexity: O(n)
        n = len(obstacleGrid[0])
        f = [0] * (n + 1)
        f[1] = 1
        for row in obstacleGrid:
            for j, x in enumerate(row):
                if x == 0:
                    f[j + 1] += f[j]
                else:
                    f[j + 1] = 0
        return f[n]


        # Method 2: dp
        # time complexity: O(mn)
        # space complexity: O(mn)
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # special case: if the start grid is obstacle, cannot go anywhere
        if obstacleGrid[0][0]==1:
            return 0
        
        # f[i][j]: the unique path to arrive grid[i][j]
        # if a grid ts an obstacle, then f[i][j] = 0
        f = [[0] * n for _ in range(m)]
        f[0][0] = 1
        for i in range(m):
            for j in range(n):
                # if f[i][j] is obstacle, skip it:
                if obstacleGrid[i][j]:
                    continue
                # if f[i][j] is space:
                if i-1 >= 0:
                    f[i][j] += f[i-1][j]
                if j-1 >= 0:
                    f[i][j] += f[i][j-1]

        return f[m-1][n-1]


        # Method 1: dfs
        # time complexity: O(mn)
        # space complexity: O(mn)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dfs(i, j): the unique paths to arrive grid[i][j]
        @cache
        def dfs(i, j):
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m-1, n-1)
# @lc code=end

