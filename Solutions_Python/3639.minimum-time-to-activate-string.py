#
# @lc app=leetcode id=3639 lang=python3
#
# [3639] Minimum Time to Activate String
#

# @lc code=start
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:

        # Method 1: Bineary Search
        # time complexity: O(NlogN)
        # space complexity: O(N)
        n = len(s)
        # replace all characters with *, the max #substring = (n+1)n/2
        if n * (n + 1) // 2 < k:
            return -1

        star = [0] * n

        # check if change orders[:m+1] to *, can we get #substrings >= k
        def check(m: int) -> bool:
            m += 1
            for j in range(m):
                star[order[j]] = m
            cnt = 0
            # the index of last `*`
            last = -1
            for i, x in enumerate(star):
                # if star[i] is `*`
                if x == m:
                    last = i
                # additively update cnt
                cnt += last + 1
                # early stopping
                if cnt >= k:
                    return True
            return False

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            # if mid satisfies condition, continue search left side
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# @lc code=end

