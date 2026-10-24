#
# @lc app=leetcode id=3296 lang=python3
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#

# @lc code=start
import bisect
import math
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Method 1: Binary Seaerch
        # time complexity: O(NlogU), U=right, N=len(workerTimes)
        # space complexity: O(1)
        # check if each worker uses at most `m` seconds, could all workers reduce the mountain
        # use binary search to find the minimal `m`
        def check(m: int) -> bool:
            left_h = mountainHeight
            for t in workerTimes:
                # assume workerTimes[i] = t, worker i reduce x units
                # then we should have x(x-1)/2 <= m/t := k
                # solve, we get x <= (-1 + sqrt(m/t + 1)) / 2
                left_h -= (math.sqrt(m // t * 8 + 1) - 1) // 2
                if left_h <= 0:
                    return True
            return False

        # the lower bound of possible time is 0
        left = 0
        # the upper bound of possible time is max_t * h(h+1)/2
        # assume all workers has the slowest workTime, each of them reduce h = ceil(mountainHeight/n) units
        max_t = max(workerTimes)
        h = (mountainHeight - 1) // len(workerTimes) + 1
        right = max_t * h * (h + 1) // 2
        while left <= right:
            mid = (left + right) // 2
            # if mid is enough to reduce the mountain, keep search left side
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
        

# @lc code=end

