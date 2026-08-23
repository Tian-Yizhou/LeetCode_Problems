#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        for c in range(cols):
            new_row = []
            for r in range(rows):
                new_row.append(matrix[r][c])
            ans.append(new_row)

        return ans
# @lc code=end

