#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Method 3: dp, optimize method 2 space complexity to O(n)
        # we only use f[i-1][j] once, so we can overwrite it
        # time complexity: O(mn)
        # space complexity: O(n)
        f = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                f[j] = f[j-1] + f[j]

        return f[n-1]

        # Method 2: dp
        # time complexity: O(mn)
        # space complexity: O(mn)
        # f[i][j]: the unique path to arrive grid[i][j]
        # initial: the 0 row and 0 column will be all 1
        f = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]

        return f[m-1][n-1]

    
        # Method 1: dfs
        # time complexity: O(mn)
        # space complexity: O(mn)

        # dfs(i, j): the unique paths to arrive grid[i][j]
        @cache
        def dfs(i, j):
            if i<0 or j<0:
                return 0
            return dfs(i-1, j) + dfs(i, j-1)

        return dfs(m-1, n-1)
    

# @lc code=end

