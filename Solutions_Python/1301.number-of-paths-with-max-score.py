'''
Author: Hannah
Date: 2026-09-26 14:38:24
LastEditTime: 2026-09-26 16:01:09
'''
#
# @lc app=leetcode id=1301 lang=python3
#
# [1301] Number of Paths with Max Score
#

# @lc code=start
# from math import inf
class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:

        MOD = 1_000_000_007
        m, n = len(board), len(board[0])

        # Method 2: DP, optimize method 1
        # time complexity: O(mn）
        # space complexity: O(n)
        max_sum = [-inf] * (n+1)
        ways = [0] * (n+1)
        # we only need down, right, down-right to update a value

        for i in range(m-1, -1, -1):
            # down-right will be covered by right, so we need to store it before update right
            down_right_sum, down_right_ways = -inf, 0

            for j in range(n-1, -1, -1):
                char = board[i][j]
                # record current sum and ways before update
                cur_sum, cur_ways = max_sum[j], ways[j]
                
                if char == 'X':
                    max_sum[j], ways[j] = -inf, 0
                elif char == 'S':
                    max_sum[j], ways[j] = 0, 1
                else:
                    s = max(max_sum[j], max_sum[j+1], down_right_sum)
                    ways[j] = 0
                    if max_sum[j] == s:
                        ways[j] += cur_ways
                    if max_sum[j+1] == s:
                        ways[j] += ways[j+1]
                    if down_right_sum == s:
                        ways[j] += down_right_ways
                    max_sum[j] = s
                    if char.isdigit():
                        max_sum[j] += int(char)
                # update down-right (sum, way) to cur (sum, way)
                down_right_sum, down_right_ways = cur_sum, cur_ways

        if max_sum[0] > -inf:
            return [max_sum[0], ways[0] % MOD]
        else:
            return [0, 0]


        # Method 1: DP
        # time complexity: O(mn)
        # space complexity: O(mn)
        max_sum = [[-inf] * (n+1) for _ in range(m+1)]
        ways = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                char = board[i][j]
                # if char is 'S', set the value
                if char == 'S':
                    max_sum[i][j] = 0
                    ways[i][j] = 1
                    continue
                # if char is 'X', do nothing
                if char == 'X':
                    continue

                s = max(max_sum[i+1][j], max_sum[i][j+1], max_sum[i+1][j+1])
                max_sum[i][j] = s
                if max_sum[i+1][j] == s:
                    ways[i][j] += ways[i+1][j]
                if max_sum[i][j+1] == s:
                    ways[i][j] += ways[i][j+1]
                if max_sum[i+1][j+1] == s:
                    ways[i][j] += ways[i+1][j+1]
                # if current char is a number (not 'E'), add its value
                if char.isdigit():
                    max_sum[i][j] += int(char)

        if max_sum[0][0] > -inf:
            return [max_sum[0][0], ways[0][0] % MOD]
        else:
            return [0, 0]




# @lc code=end

