#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
from functools import cache
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        n_strs = len(strs)

        # Method 3: dp, optimize space complexity to O(mn)
        # we only need f[i] when get f[i+1]
        f = [[0] * (n+1) for _ in range(m+1)]
        for i, s in enumerate(strs):
            cnt_0 = s.count('0')
            cnt_1 = len(s) - cnt_0
            # reverse iteration to update
            for m_left in range(m, cnt_0-1, -1):
                for n_left in range(n, cnt_1-1, -1):
                    f[m_left][n_left] = max(f[m_left][n_left], f[m_left - cnt_0][n_left - cnt_1] + 1)

        return f[m][n]


        # Method 2: dp
        # time complexity: O(len(strs)mn)
        # space complexity: O(len(strs)mn)
        f = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(n_strs + 1)]
        for i, s in enumerate(strs):
            cnt_0 = s.count('0')
            cnt_1 = len(s) - cnt_0
            for m_left in range(m + 1):
                for n_left in range(n + 1):
                    # if we have capacity, we can select or not select
                    if m_left >= cnt_0 and n_left >= cnt_1:
                        f[i + 1][m_left][n_left] = max(f[i][m_left][n_left], f[i][m_left - cnt_0][n_left - cnt_1] + 1)
                    # if we don't have capacity, we cannot select
                    else:
                        f[i + 1][m_left][n_left] = f[i][m_left][n_left]
        return f[-1][m][n]

        # Method 1: dfs
        # time complexity: O(len(strs)mn)
        # space complexity: O(len(strs)mn)
        cnt = [(s.count('0'), s.count('1')) for s in strs]
        # dfs(i, m_left, n_left): the number of elements of max subset 
        # when come to strs[i], with m_left is remian #0, n_left is remian #1
        @cache
        def dfs(i, m_left, n_left):
            # boundary
            # if we don't have capacity, invalid
            if m_left < 0 or n_left < 0:
                return -inf
            if i < 0:
                return 0

            cnt_0, cnt_1 = cnt[i]
            # if select strs[i], dfs(i, m_left, n_left) = dfs(i-1, m_left + cnt_0, n_left + cnt_1) + 1
            # if not select strs[i], dfs(i, m_left, n_left) = dfs(i-1, m_left, n_left)
            return max(dfs(i-1, m_left - cnt_0, n_left - cnt_1) + 1, dfs(i-1, m_left, n_left))

        return dfs(n_strs-1, m, n)
# @lc code=end

