'''
Author: Hannah
Date: 2026-02-01 11:29:04
LastEditTime: 2026-03-20 15:46:20
'''
#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        # apply bisect to the row index of the matrix
        # open interval: (-1, n-1)
        left, right = -1, len(mat) - 1

        while left + 1 < right:
            # find the max element of mid row
            cur_row = (left + right) // 2
            mx = max(mat[cur_row])
            # if mx > the largest element of next row
            if mx > mat[cur_row + 1][mat[cur_row].index(mx)]:
                # peak is in current row or above rows
                right = cur_row
            # if mx < the largest element of next row
            else:
                # peak is in next row or rows under it
                left = cur_row
        # the row index of peak element is right
        # and find the largest element of this row
        return [right, mat[right].index(max(mat[right]))]

# @lc code=end

