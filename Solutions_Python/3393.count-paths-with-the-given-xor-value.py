#
# @lc app=leetcode id=3393 lang=python3
#
# [3393] Count Paths With the Given XOR Value
#

# @lc code=start
from functools import cache
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:

        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])

        # Method 2: dp
        u = 1 << max(map(max, grid)).bit_length()
        if k >= u:
            return 0

        m, n = len(grid), len(grid[0])
        f = [[[0] * u for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = 1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                for x in range(u):
                    f[i + 1][j + 1][x] = (f[i + 1][j][x ^ val] + f[i][j + 1][x ^ val]) % MOD
        return f[m][n][k]


        # Method 1: dfs
        # time conplexity: O(mnU), U=max(grid[i][j])
        # space complexity: O(mnU)
        # dfs(i, j, x): the paths to arrive grid[i][j] with XOR value x
        @cache
        def dfs(i, j, x):
            if i < 0 or j < 0:
                # no path if exceed boundary
                return 0
            val = grid[i][j]
            if i == 0 and j == 0:
                # if the XOR value of start grid is itself, then #path = 1;
                # otherwise, #path = 0
                return 1 if x==val else 0
            # y ^ val = x -> y = x ^ val
            return (dfs(i-1, j, x ^ val) + dfs(i, j, x ^ val)) % MOD

        ans = dfs(m-1, n-1, k)
        dfs.cache_clear()

        return ans

# @lc code=end

