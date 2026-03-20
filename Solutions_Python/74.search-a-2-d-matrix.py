'''
Author: Hannah
Date: 2026-02-01 11:28:57
LastEditTime: 2026-03-20 15:01:57
'''
#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        # start from the 0 row
        cur_row = 0

        # when there is a row
        while cur_row < m:
            # if target < the smallest number, we cannot find target
            if target < matrix[cur_row][0]:
                return False
            # if target > the largest number,
            if target > matrix[cur_row][n-1]:
                # if there is a row, move to next row
                if cur_row < m-1:
                    cur_row += 1
                    continue
                # if cur_row is the last row, we cannot find target
                else:
                    return False
            
            # target might in current row
            # use bisect to find whether target is in current row
            # open interval (-1, n); close interval [0, n -1]
            left, right = -1, n
            while left + 1 < right:
                mid = (left + right) // 2
                if matrix[cur_row][mid] == target:
                    # we find target
                    return True
                elif matrix[cur_row][mid] < target:
                    # mid and its left < target
                    left = mid
                else:
                    # mid and its right > target
                    right = mid
            # then matrix[cur_row][right] is the first number >  target
            return False

# @lc code=end

