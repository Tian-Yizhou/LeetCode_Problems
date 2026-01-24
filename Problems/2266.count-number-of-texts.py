'''
Author: Hannah
Date: 2026-01-24 00:46:14
LastEditTime: 2026-01-24 01:48:41
'''
#
# @lc app=leetcode id=2266 lang=python3
#
# [2266] Count Number of Texts
#

# @lc code=start
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        
        mod = 10 ** 9 + 7
        f = [1, 1, 2, 4]
        g = [1, 1, 2, 4]
        n = len(pressedKeys)
        for i in range(4, n + 1):
            f.append((f[i-1] + f[i-2] + f[i-3]) % mod)
            g.append((g[i-1] + g[i-2] + g[i-3] + g[i-4]) % mod)

        ans = 1
        for ch, s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans * (g[m] if ch in "79" else f[m]) % mod
        
        return ans

# @lc code=end

