#
# @lc app=leetcode id=2106 lang=python3
#
# [2106] Maximum Fruits Harvested After at Most K Steps
#

# @lc code=start
# import bisect
class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        # Method: Sliding window
        # time complexity: O(N), N=len(fruits)
        # space complexity: O(1)
        # iterate the left end of the valid window, in which
        # all fruits can be picked

        # initially, we start at the most left position, 
        # all fruits are on the left side of startPos
        left = bisect.bisect_left(fruits, startPos-k, key=lambda x: x[0])
        right = bisect.bisect_left(fruits, startPos+1, key=lambda x: x[0])
        ans = s = sum(f[1] for f in fruits[left:right])

        # right cannot exceed fruits; the most right position is startPos+k
        # assume fruits[right] can be picked, add it into s
        while right < n and fruits[right][0] <= startPos+k:
            s += fruits[right][1]
            # ensure left is valid(can be achieved within k steps)
            # if first goes left, then right, the total step is fruits[right][0] - startPos + fruits[right][0] - fruits[left][0]
            # if first goes right, then left, the total step is startPos - fruits[left][0] + fruits[right][0] - fruits[left][0]
            while fruits[right][0] - startPos + fruits[right][0] - fruits[left][0] > k and \
                  startPos - fruits[left][0] + fruits[right][0] - fruits[left][0] > k:
                s -= fruits[left][1]
                left += 1

            # now the window is valid, update answer
            ans = max(ans, s)

            # move right end of the window
            right += 1

        return ans

# @lc code=end

