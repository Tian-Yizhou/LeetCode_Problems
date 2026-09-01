#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        # Method 2: dp, optimize space complexity to O(n)
        pre_f = matrix[0]

        for i in range(1, n):
            cur_f = [0] * n
            for j in range(n):
                if j == 0:
                    cur_f[j] = min(pre_f[j], pre_f[j+1]) + matrix[i][j]
                elif j == n-1:
                    cur_f[j] = min(pre_f[j-1], pre_f[j]) + matrix[i][j]
                else:
                    cur_f[j] = min(pre_f[j-1], pre_f[j], pre_f[j+1]) + matrix[i][j]
            pre_f = cur_f

        return min(pre_f)


        # Method 1: dp
        # time complexity: O(n^2)
        # space complexity: O(n^2)
        f = [[0] * n for _ in range(n)]
        f[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                # left boundary
                if j == 0:
                    f[i][j] = min(f[i-1][j], f[i-1][j+1]) + matrix[i][j]
                # right boundary
                elif j == n-1:
                    f[i][j] = min(f[i-1][j-1], f[i-1][j]) + matrix[i][j]
                else:
                    f[i][j] = min(f[i-1][j-1], f[i-1][j], f[i-1][j+1]) + matrix[i][j]

        return min(f[-1])
# @lc code=end

