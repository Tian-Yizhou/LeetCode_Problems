#
# @lc app=leetcode id=3679 lang=python3
#
# [3679]  Minimum Discards to Balance Inventory
#

# @lc code=start
from collections import Counter
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        n = len(arrivals)
        discarded = [False] * n
        cnt = Counter()
        ans = 0

        for i, t in enumerate(arrivals):
            # if the item exceeds inventory, discard it
            if cnt[t] == m:
                discarded[i] = True
                ans += 1
            # otherwise, keep it
            else:
                cnt[t] += 1

            # sliding window, remove left item
            if i >= w - 1:
                left_idx = i - w + 1
                if not discarded[left_idx]:
                    cnt[arrivals[left_idx]] -= 1

        return ans


# @lc code=end

