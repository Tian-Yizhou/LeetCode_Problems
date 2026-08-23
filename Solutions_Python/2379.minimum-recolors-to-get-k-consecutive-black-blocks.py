#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
# from math import inf
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # time complexity: O(n)
        n = len(blocks)
        ans = 0
        for i in range(k):
            if blocks[i] == 'W':
                ans += 1

        cnt = ans
        # sliding window
        for right in range(k, n):
            if blocks[right] == 'W':
                cnt += 1
            if blocks[right-k] == 'W':
                cnt -= 1
            ans = min(ans, cnt)

        return ans
# @lc code=end

